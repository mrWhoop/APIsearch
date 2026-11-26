import pymongo
import scipy.stats
from pymongo import MongoClient
from pymongo.errors import OperationFailure
from pathlib import Path
import json
from itertools import combinations
from collections import Counter
import os
from dotenv import load_dotenv
import json
import time
import math
import itertools

from scipy.stats import wilcoxon
from scipy.stats import bootstrap

import pandas as pd
from statsmodels.stats.multitest import multipletests



load_dotenv()

client = MongoClient(os.environ['MONGO_READWRITE_URI'])
db = client["api"]
collection = db["searchEvaluation"]


import itertools
import numpy as np
import pandas as pd

from scipy.stats import wilcoxon, bootstrap
from statsmodels.stats.multitest import multipletests


component_a = [
        "OpenAISimple",
        "OpenAIStructured",
        "OpenAIDescriptive",
        # "GeminiSimple",
        # "GeminiStructured",
        # "GeminiDescriptive",
        # "OpenAIPrompt",
        # "GeminiPrompt",
        # "Meilisearch",
        # "MeilisearchEmbed",
    ]

component_b = [
    "OpenAISimple",
    "OpenAIStructured",
    "OpenAIDescriptive",
    # "GeminiSimple",
    # "GeminiStructured",
    # "GeminiDescriptive",
    # "OpenAIPrompt",
    # "GeminiPrompt",
    # "Meilisearch",
    # "MeilisearchEmbed",
]

def query_type_filter(queryType):
    """Build the Mongo filter for queryType: None, a single value, or a list."""
    if queryType is None:
        return None
    if isinstance(queryType, (list, tuple, set)):
        values = list(queryType)
        if not values:
            raise ValueError("queryType list is empty")
        return {"$in": values}
    return queryType


def fetch_scores(component, queryType, metric):
    """Return {(queryType, query): score} for one component.

    queryType may be None (all types), a single value, or a list of values.
    """
    match = {"component": component}
    qt_filter = query_type_filter(queryType)
    if qt_filter is not None:
        match["queryType"] = qt_filter

    if metric == "s5":
        # "specific" queries use the corrected s5 value
        value = {
            "$cond": [
                {"$eq": ["$queryType", "specific"]},
                "$s5_replace",
                "$s5",
            ]
        }
    else:
        value = f"${metric}"

    documents = collection.aggregate([
        {"$match": match},
        {"$project": {"_id": 0, "query": 1, "queryType": 1, "score": value}},
        {"$sort": {"query": 1}},
    ])

    scores = {}
    for doc in documents:
        key = (doc.get("queryType"), doc["query"])
        if key in scores:
            raise ValueError(f"Duplicate entry for {component}: {key}")
        scores[key] = doc.get("score")
    return scores


def mean_difference(a, b, axis=-1):
    return np.mean(a - b, axis=axis)

# popravljeno in dopolnjeno z UI
def wilk(queryType, metric, component_a, component_b, file_name):
    # de-duplicate within each list, keeping order
    component_a = list(dict.fromkeys(component_a))
    component_b = list(dict.fromkeys(component_b))

    # fetch each component once, even if it appears in both lists
    all_components = list(dict.fromkeys(component_a + component_b))
    scores = {c: fetch_scores(c, queryType, metric) for c in all_components}

    results = []
    seen_pairs = set()

    for system_a, system_b in itertools.product(component_a, component_b):

        # no self-comparison
        if system_a == system_b:
            continue

        # count (X, Y) and (Y, X) only once
        pair = frozenset((system_a, system_b))
        if pair in seen_pairs:
            continue
        seen_pairs.add(pair)

        sa, sb = scores[system_a], scores[system_b]
        common_queries = sorted(set(sa) & set(sb), key=str)

        if not common_queries:
            continue

        a = np.asarray([sa[q] for q in common_queries], dtype=float)
        b = np.asarray([sb[q] for q in common_queries], dtype=float)

        if not np.isfinite(a).all() or not np.isfinite(b).all():
            raise ValueError(
                f"Missing or non-finite scores for {system_a} vs {system_b}"
            )

        mean_a = np.mean(a)
        mean_b = np.mean(b)
        observed_difference = np.mean(a - b)

        # Wilcoxon signed-rank test
        if np.all(a == b):
            statistic, p_value = 0.0, 1.0
            continue
        else:
            test = wilcoxon(a, b, alternative="two-sided")
            statistic, p_value = test.statistic, test.pvalue

        # Paired bootstrap 95% CI of mean difference
        boot = bootstrap(
            (a, b),
            mean_difference,
            paired=True,
            vectorized=True,
            n_resamples=50_000,
            confidence_level=0.95,
            method="percentile",
            rng=np.random.default_rng(42),
        )
        ci_lower = boot.confidence_interval.low
        ci_upper = boot.confidence_interval.high

        results.append({
            "component_a": system_a,
            "component_b": system_b,
#            "n_queries": len(common_queries),
#            "mean_a": mean_a,
#            "mean_b": mean_b,
            "mean_difference": observed_difference,
            "ci_lower": ci_lower,
            "ci_upper": ci_upper,
#            "bootstrap_significant": ci_lower > 0 or ci_upper < 0,
#            "statistic": statistic,
            "p_value": p_value,
            "p_significant": p_value < 0.05,
        })

    df = pd.DataFrame(results)

    if not df.empty:
        # Holm correction across all A-vs-B comparisons
        df["p_adjusted"] = multipletests(df["p_value"], method="holm")[1]
        df["significant"] = df["p_adjusted"] <= 0.05

        df = df.sort_values("p_adjusted")
        print(df.to_string(index=False))

    df.to_csv(file_name, index=False)
    return df

def precision_at_5(queryType, component):

    evaluations = collection.find({"queryType": queryType, "component": component})

    scores = []

    for evaluation in evaluations:
        accepted = evaluation.get("accepted")
        score = len(accepted) / 5
        scores.append(score)

        collection.update_one(
            {"_id": evaluation["_id"]},
            {"$set": {"precision5": score}}
        )

    print(component, sum(scores) / len(scores) if scores else 0.0, len(scores))
    return sum(scores) / len(scores) if scores else 0.0

def ndcg_at_5(queryType, component):
    evaluations = collection.find({
        "queryType": queryType,
        "component": component
    })

    scores = []

    for evaluation in evaluations:
        relevance = {}

        for item in evaluation.get("accepted", []):
            relevance[item["position"]] = 1

        for item in evaluation.get("rejected", []):
            relevance[item["position"]] = 0

        # DCG@5
        dcg = sum(
            relevance.get(position, 0) / math.log2(position + 1)
            for position in range(1, 6)
        )

        # Ideal DCG@5 relevance needs to be based across all systems on the same query
        resForQuery = evaluation.get("query")
        allForQuery = collection.find({"query": resForQuery})
        allRelevant = set()
        for res in allForQuery:
            acc = res.get("accepted")
            for a in acc:
                allRelevant.add(a["id"])

        maxRelevant = min(len(allRelevant), 5)

        idcg = sum(
            1 / math.log2(position + 1)
            for position in range(1, maxRelevant + 1)
        )

        # nDCG@5

        score = dcg / idcg if idcg > 0 else 0.0
        scores.append(score)

        collection.update_one(
            {"_id": evaluation["_id"]},
            {"$set": {"ndcg5": score}}
        )

    print(component, sum(scores) / len(scores) if scores else 0.0, len(scores))
    return sum(scores) / len(scores) if scores else 0.0

def score_at_5():
    evaluations = collection.find({})

    for evaluation in evaluations:
        p5 = evaluation.get("precision5")
        ndcg5 = evaluation.get("ndcg5")
        try:
            s5 = (p5 + ndcg5)/2
        except TypeError:
            print(evaluation["_id"])

        collection.update_one(
            {"_id": evaluation["_id"]},
            {"$set": {"s5": s5}}
        )

# score_at_5()

def score_eval(queryType):
    print("OpenAISimple ", (precision_at_5(queryType, "OpenAISimple") + ndcg_at_5(queryType, "OpenAISimple")) / 2)
    print("OpenAIStructured ", (precision_at_5(queryType, "OpenAIStructured") + ndcg_at_5(queryType, "OpenAIStructured")) / 2)
    print("OpenAIDescriptive ", (precision_at_5(queryType, "OpenAIDescriptive") + ndcg_at_5(queryType, "OpenAIDescriptive")) / 2)

    print("Meilisearch ", (precision_at_5(queryType, "Meilisearch") + ndcg_at_5(queryType, "Meilisearch")) / 2)
    print("MeilisearchEmbed ", (precision_at_5(queryType, "MeilisearchEmbed") + ndcg_at_5(queryType, "MeilisearchEmbed")) / 2)

    print("GeminiSimple ", (precision_at_5(queryType, "GeminiSimple") + ndcg_at_5(queryType, "GeminiSimple")) / 2)
    print("GeminiStructured ", (precision_at_5(queryType, "GeminiStructured") + ndcg_at_5(queryType, "GeminiStructured")) / 2)
    print("GeminiDescriptive ", (precision_at_5(queryType, "GeminiDescriptive") + ndcg_at_5(queryType, "GeminiDescriptive")) / 2)

    print("OpenAIPrompt ", (precision_at_5(queryType, "OpenAIPrompt") + ndcg_at_5(queryType, "OpenAIPrompt")) / 2)
    print("GeminiPrompt ", (precision_at_5(queryType, "GeminiPrompt") + ndcg_at_5(queryType, "GeminiPrompt")) / 2)


print("-------------- SIMPLE P5 --------------" )

# precision_at_5("simple", "OpenAISimple")
# precision_at_5("simple", "OpenAIStructured")
# precision_at_5("simple", "OpenAIDescriptive")
#
# precision_at_5("simple", "Meilisearch")
# precision_at_5("simple", "MeilisearchEmbed")
#
# precision_at_5("simple", "GeminiSimple")
# precision_at_5("simple", "GeminiStructured")
# precision_at_5("simple", "GeminiDescriptive")

# precision_at_5("simple", "OpenAIPrompt")
# precision_at_5("simple", "GeminiPrompt")

print("-------------- NAMED P5 --------------" )

# precision_at_5("named", "OpenAISimple")
# precision_at_5("named", "OpenAIStructured")
# precision_at_5("named", "OpenAIDescriptive")
#
# precision_at_5("named", "Meilisearch")
# precision_at_5("named", "MeilisearchEmbed")
#
# precision_at_5("named", "GeminiSimple")
# precision_at_5("named", "GeminiStructured")
# precision_at_5("named", "GeminiDescriptive")

# precision_at_5("named", "OpenAIPrompt")
# precision_at_5("named", "GeminiPrompt")

print("-------------- COMPLEX P5 --------------" )

# precision_at_5("complex", "OpenAISimple")
# precision_at_5("complex", "OpenAIStructured")
# precision_at_5("complex", "OpenAIDescriptive")
#
# precision_at_5("complex", "Meilisearch")
# precision_at_5("complex", "MeilisearchEmbed")
#
# precision_at_5("complex", "GeminiSimple")
# precision_at_5("complex", "GeminiStructured")
# precision_at_5("complex", "GeminiDescriptive")

# precision_at_5("complex", "OpenAIPrompt")
# precision_at_5("complex", "GeminiPrompt")

print("-------------- SIMPLE ndcg5 --------------" )

# ndcg_at_5("simple", "OpenAISimple")
# ndcg_at_5("simple", "OpenAIStructured")
# ndcg_at_5("simple", "OpenAIDescriptive")
#
# ndcg_at_5("simple", "Meilisearch")
# ndcg_at_5("simple", "MeilisearchEmbed")
#
# ndcg_at_5("simple", "GeminiSimple")
# ndcg_at_5("simple", "GeminiStructured")
# ndcg_at_5("simple", "GeminiDescriptive")

# ndcg_at_5("simple", "OpenAIPrompt")
# ndcg_at_5("simple", "GeminiPrompt")

print("-------------- NAMED ndcg5 --------------" )

# ndcg_at_5("named", "OpenAISimple")
# ndcg_at_5("named", "OpenAIStructured")
# ndcg_at_5("named", "OpenAIDescriptive")
#
# ndcg_at_5("named", "Meilisearch")
# ndcg_at_5("named", "MeilisearchEmbed")
#
# ndcg_at_5("named", "GeminiSimple")
# ndcg_at_5("named", "GeminiStructured")
# ndcg_at_5("named", "GeminiDescriptive")

# ndcg_at_5("named", "OpenAIPrompt")
# ndcg_at_5("named", "GeminiPrompt")

print("-------------- COMPLEX ndcg5 --------------" )

# ndcg_at_5("complex", "OpenAISimple")
# ndcg_at_5("complex", "OpenAIStructured")
# ndcg_at_5("complex", "OpenAIDescriptive")
#
# ndcg_at_5("complex", "Meilisearch")
# ndcg_at_5("complex", "MeilisearchEmbed")
#
# ndcg_at_5("complex", "GeminiSimple")
# ndcg_at_5("complex", "GeminiStructured")
# ndcg_at_5("complex", "GeminiDescriptive")

# ndcg_at_5("complex", "OpenAIPrompt")
# ndcg_at_5("complex", "GeminiPrompt")

print("-------------- SIMPLE stat-test --------------" )
# score_eval("simple")
# wilk("simple", "precision5", component_a, component_b, "enostavne_poizvedbe_PrecisionRate5.csv")
# wilk("simple", "ndcg5", component_a, component_b,"enostavne_poizvedbe_ndcgRate5.csv")
# wilk("simple", "s5", components, "enostavne_poizvedbe_S5.csv")

print("-------------- NAMED stat-test --------------" )
# score_eval("named")
# wilk("named", "precision5", components, "poimenske_poizvedbe_PrecisionRate5.csv")
# wilk("named", "ndcg5", component_a, component_b, "poimenske_poizvedbe_ndcgRate5.csv")
# wilk("named", "s5", components, "poimenske_poizvedbe_s5.csv")

print("-------------- COMPLEX stat-test --------------" )
# score_eval("complex")
# wilk("complex", "precision5", components, "sestavljene_poizvedbe_PrecisionRate5.csv")
# wilk("complex", "ndcg5", component_a, component_b, "sestavljene_poizvedbe_ndcgRate5.csv")
# wilk("complex", "s5", components, "sestavljene_poizvedbe_s5.csv")

def mrr(queryType, component):
    evaluations = collection.find({
        "queryType": queryType,
        "component": component
    })

    reciprocal_ranks = []

    for evaluation in evaluations:
        marked = evaluation.get("marked")

        score = 0.0

        if marked and marked.get("position", 0) > 0:
            score = 1 / marked["position"]
            reciprocal_ranks.append(score)
        else:
            reciprocal_ranks.append(0.0)

        collection.update_one(
            {"_id": evaluation["_id"]},
            {"$set": {"rr": score}}
        )

    print(component, sum(reciprocal_ranks) / len(reciprocal_ranks) if reciprocal_ranks else 0.0)
    return sum(reciprocal_ranks) / len(reciprocal_ranks) if reciprocal_ranks else 0.0

def hit_at_1(queryType, component):
    evaluations = collection.find({
            "queryType": queryType,
            "component": component
        })

    hit = 0
    total = 0
    for evaluation in evaluations:
        if evaluation.get("marked"):
            hit += 1
            total += 1

            collection.update_one(
                {"_id": evaluation["_id"]},
                {"$set": {"hit": 1.0}}
            )

        else:

            collection.update_one(
                {"_id": evaluation["_id"]},
                {"$set": {"hit": 0.0}}
            )

            total += 1

    print(component, hit / total if total else 0.0)
    return hit / total if total else 0.0

print("-------------- NAMED Hit@1 --------------" )

# hit_at_1("named", "OpenAISimple")
# hit_at_1("named", "OpenAIStructured")
# hit_at_1("named", "OpenAIDescriptive")
#
# hit_at_1("named", "Meilisearch")
# hit_at_1("named", "MeilisearchEmbed")
#
# hit_at_1("named", "GeminiSimple")
# hit_at_1("named", "GeminiStructured")
# hit_at_1("named", "GeminiDescriptive")
#
# hit_at_1("named", "OpenAIPrompt")
# hit_at_1("named", "GeminiPrompt")

print("-------------- NAMED MRR --------------" )

# mrr("named", "OpenAISimple")
# mrr("named", "OpenAIStructured")
# mrr("named", "OpenAIDescriptive")
#
# mrr("named", "Meilisearch")
# mrr("named", "MeilisearchEmbed")
#
# mrr("named", "GeminiSimple")
# mrr("named", "GeminiStructured")
# mrr("named", "GeminiDescriptive")
#
# mrr("named", "OpenAIPrompt")
# mrr("named", "GeminiPrompt")

def mrr_replacement(queryType, component):
    evaluations = collection.find({
        "queryType": queryType,
        "component": component
    })

    reciprocal_ranks = []

    for evaluation in evaluations:
        marked = evaluation.get("marked")

        score = 0.0

        if marked and marked.get("position", 0) > 0:
            score = 1 / marked["position"]
            reciprocal_ranks.append(score)
        else:
            accepted = evaluation.get("accepted")
            if len(accepted) == 1:
                score = 1 / accepted[0]["position"]
                reciprocal_ranks.append(score)
            else:
                reciprocal_ranks.append(0.0)

        collection.update_one(
            {"_id": evaluation["_id"]},
            {"$set": {"rr_replace": score}}
        )


    print(component, sum(reciprocal_ranks) / len(reciprocal_ranks) if reciprocal_ranks else 0.0)
    return sum(reciprocal_ranks) / len(reciprocal_ranks) if reciprocal_ranks else 0.0

print("-------------- SPECIFIC MMR --------------" )

# mrr("specific", "OpenAISimple")
# mrr("specific", "OpenAIStructured")
# mrr("specific", "OpenAIDescriptive")
#
# mrr("specific", "Meilisearch")
# mrr("specific", "MeilisearchEmbed")
#
# mrr("specific", "GeminiSimple")
# mrr("specific", "GeminiStructured")
# mrr("specific", "GeminiDescriptive")

# mrr("specific", "OpenAIPrompt")
# mrr("specific", "GeminiPrompt")

print("-------------- SPECIFIC MMR replacement --------------" )

# mrr_replacement("specific", "OpenAISimple")
# mrr_replacement("specific", "OpenAIStructured")
# mrr_replacement("specific", "OpenAIDescriptive")
#
# mrr_replacement("specific", "Meilisearch")
# mrr_replacement("specific", "MeilisearchEmbed")
#
# mrr_replacement("specific", "GeminiSimple")
# mrr_replacement("specific", "GeminiStructured")
# mrr_replacement("specific", "GeminiDescriptive")

# mrr_replacement("specific", "OpenAIPrompt")
# mrr_replacement("specific", "GeminiPrompt")

print("-------------- SPECIFIC Hit@1 --------------" )

# hit_at_1("specific", "OpenAISimple")
# hit_at_1("specific", "OpenAIStructured")
# hit_at_1("specific", "OpenAIDescriptive")
#
# hit_at_1("specific", "Meilisearch")
# hit_at_1("specific", "MeilisearchEmbed")
#
# hit_at_1("specific", "GeminiSimple")
# hit_at_1("specific", "GeminiStructured")
# hit_at_1("specific", "GeminiDescriptive")

# hit_at_1("specific", "OpenAIPrompt")
# hit_at_1("specific", "GeminiPrompt")

print("-------------- SPECIFIC Hit@1 replacement --------------" )

def hit_at_1_replacement(queryType, component):
    evaluations = collection.find({
            "queryType": queryType,
            "component": component
        })

    hit = 0
    total = 0
    for evaluation in evaluations:
        if evaluation.get("marked"):
            hit += 1

            collection.update_one(
                {"_id": evaluation["_id"]},
                {"$set": {"hit_replace": 1.0}}
            )

            total += 1
        elif len(evaluation.get("accepted")) == 1:
            hit += 1

            collection.update_one(
                {"_id": evaluation["_id"]},
                {"$set": {"hit_replace": 1.0}}
            )

            total += 1
        else:

            collection.update_one(
                {"_id": evaluation["_id"]},
                {"$set": {"hit_replace": 0.0}}
            )

            total += 1

    print(component, hit / total if total else 0.0)
    return hit / total if total else 0.0

# hit_at_1_replacement("specific", "OpenAISimple")
# hit_at_1_replacement("specific", "OpenAIStructured")
# hit_at_1_replacement("specific", "OpenAIDescriptive")
#
# hit_at_1_replacement("specific", "Meilisearch")
# hit_at_1_replacement("specific", "MeilisearchEmbed")
#
# hit_at_1_replacement("specific", "GeminiSimple")
# hit_at_1_replacement("specific", "GeminiStructured")
# hit_at_1_replacement("specific", "GeminiDescriptive")

# hit_at_1_replacement("specific", "OpenAIPrompt")
# hit_at_1_replacement("specific", "GeminiPrompt")

def score_at_5_specific():
    evaluations = collection.find({"queryType":"specific"})

    for evaluation in evaluations:
        rr = evaluation.get("rr")
        hit = evaluation.get("hit")
        try:
            s5 = (rr + hit)/2
        except TypeError:
            print(evaluation["_id"])

        collection.update_one(
            {"_id": evaluation["_id"]},
            {"$set": {"s5": s5}}
        )

def score_at_5_specific_replacement():
    evaluations = collection.find({"queryType":"specific"})

    for evaluation in evaluations:
        rr = evaluation.get("rr_replace")
        hit = evaluation.get("hit_replace")
        try:
            s5 = (rr + hit)/2
        except TypeError:
            print(evaluation["_id"])

        collection.update_one(
            {"_id": evaluation["_id"]},
            {"$set": {"s5_replace": s5}}
        )

# score_at_5_specific()
# score_at_5_specific_replacement()

def score_eval_specific(queryType):
    print("OpenAISimple ", (hit_at_1(queryType, "OpenAISimple") + mrr(queryType, "OpenAISimple")) / 2)
    print("OpenAIStructured ", (hit_at_1(queryType, "OpenAIStructured") + mrr(queryType, "OpenAIStructured")) / 2)
    print("OpenAIDescriptive ", (hit_at_1(queryType, "OpenAIDescriptive") + mrr(queryType, "OpenAIDescriptive")) / 2)

    print("Meilisearch ", (hit_at_1(queryType, "Meilisearch") + mrr(queryType, "Meilisearch")) / 2)
    print("MeilisearchEmbed ", (hit_at_1(queryType, "MeilisearchEmbed") + mrr(queryType, "MeilisearchEmbed")) / 2)

    print("GeminiSimple ", (hit_at_1(queryType, "GeminiSimple") + mrr(queryType, "GeminiSimple")) / 2)
    print("GeminiStructured ", (hit_at_1(queryType, "GeminiStructured") + mrr(queryType, "GeminiStructured")) / 2)
    print("GeminiDescriptive ", (hit_at_1(queryType, "GeminiDescriptive") + mrr(queryType, "GeminiDescriptive")) / 2)

    print("OpenAIPrompt ", (hit_at_1(queryType, "OpenAIPrompt") + mrr(queryType, "OpenAIPrompt")) / 2)
    print("GeminiPrompt ", (hit_at_1(queryType, "GeminiPrompt") + mrr(queryType, "GeminiPrompt")) / 2)

def score_eval_specific_replacement(queryType):
    print("OpenAISimple ", (hit_at_1_replacement(queryType, "OpenAISimple") + mrr_replacement(queryType, "OpenAISimple")) / 2)
    print("OpenAIStructured ", (hit_at_1_replacement(queryType, "OpenAIStructured") + mrr_replacement(queryType, "OpenAIStructured")) / 2)
    print("OpenAIDescriptive ", (hit_at_1_replacement(queryType, "OpenAIDescriptive") + mrr_replacement(queryType, "OpenAIDescriptive")) / 2)

    print("Meilisearch ", (hit_at_1_replacement(queryType, "Meilisearch") + mrr_replacement(queryType, "Meilisearch")) / 2)
    print("MeilisearchEmbed ", (hit_at_1_replacement(queryType, "MeilisearchEmbed") + mrr_replacement(queryType, "MeilisearchEmbed")) / 2)

    print("GeminiSimple ", (hit_at_1_replacement(queryType, "GeminiSimple") + mrr_replacement(queryType, "GeminiSimple")) / 2)
    print("GeminiStructured ", (hit_at_1_replacement(queryType, "GeminiStructured") + mrr_replacement(queryType, "GeminiStructured")) / 2)
    print("GeminiDescriptive ", (hit_at_1_replacement(queryType, "GeminiDescriptive") + mrr_replacement(queryType, "GeminiDescriptive")) / 2)

    print("OpenAIPrompt ", (hit_at_1_replacement(queryType, "OpenAIPrompt") + mrr_replacement(queryType, "OpenAIPrompt")) / 2)
    print("GeminiPrompt ", (hit_at_1_replacement(queryType, "GeminiPrompt") + mrr_replacement(queryType, "GeminiPrompt")) / 2)

print("-------------- SPECIFIC score --------------")
# score_eval_specific("specific")

print("-------------- SPECIFIC score replacement stat-test --------------")
# score_eval_specific_replacement("specific")

# wilk("specific", "rr_replace", component_a, component_b, "specificne_poizvedbe_mrr.csv")
# wilk("specific", "hit_replace", components, "specificne_poizvedbe_hit1.csv")
# wilk("specific", "s5_replace", components, "specificne_poizvedbe_s5.csv")

print("-------------- Metric summary --------------")

def score_summary():

    queryTypes = ['simple', 'named', 'complex']

    OpenAISimpleSum = 0.0
    OpenAIStructuredSum = 0.0
    OpenAIDescriptiveSum = 0.0

    MeilisearchSum = 0.0
    MeilisearchEmbedSum = 0.0

    GeminiSimpleSum = 0.0
    GeminiStructuredSum = 0.0
    GeminiDescriptiveSum = 0.0

    OpenAIPromptSum = 0.0
    GeminiPromptSum = 0.0

    for queryType in queryTypes:

        print('------------', queryType, '--------------')

        OpenAISimple = (ndcg_at_5(queryType, "OpenAISimple"))
        OpenAISimpleSum = OpenAISimpleSum + OpenAISimple
        print('OpenAISimple', OpenAISimple)

        OpenAIStructured = (ndcg_at_5(queryType, "OpenAIStructured"))
        OpenAIStructuredSum = OpenAIStructuredSum + OpenAIStructured
        print('OpenAIStructured', OpenAIStructured)

        OpenAIDescriptive = (ndcg_at_5(queryType, "OpenAIDescriptive"))
        OpenAIDescriptiveSum = OpenAIDescriptiveSum + OpenAIDescriptive
        print('OpenAIDescriptive', OpenAIDescriptive)

        Meilisearch = (ndcg_at_5(queryType, "Meilisearch"))
        MeilisearchSum = MeilisearchSum + Meilisearch
        print('Meilisearch', Meilisearch)

        MeilisearchEmbed = (ndcg_at_5(queryType, "MeilisearchEmbed"))
        MeilisearchEmbedSum = MeilisearchEmbedSum + MeilisearchEmbed
        print('MeilisearchEmbed', MeilisearchEmbed)

        GeminiSimple = (ndcg_at_5(queryType, "GeminiSimple"))
        GeminiSimpleSum = GeminiSimpleSum + GeminiSimple
        print('GeminiSimple', GeminiSimple)

        GeminiStructured = (ndcg_at_5(queryType, "GeminiStructured"))
        GeminiStructuredSum = GeminiStructuredSum + GeminiStructured
        print('GeminiStructured', GeminiStructured)

        GeminiDescriptive = (ndcg_at_5(queryType, "GeminiDescriptive"))
        GeminiDescriptiveSum = GeminiDescriptiveSum + GeminiDescriptive
        print('GeminiDescriptive', GeminiDescriptive)

        OpenAIPrompt = (ndcg_at_5(queryType, "OpenAIPrompt"))
        OpenAIPromptSum = OpenAIPromptSum + OpenAIPrompt
        print('OpenAIPrompt', OpenAIPrompt)

        GeminiPrompt = (ndcg_at_5(queryType, "GeminiPrompt"))
        GeminiPromptSum = GeminiPromptSum + GeminiPrompt
        print('GeminiPrompt', GeminiPrompt)

    print('------------', 'specific', '--------------')

    OpenAISimple = (mrr_replacement("specific", "OpenAISimple"))
    print('OpenAISimple', OpenAISimple)

    OpenAIStructured = (mrr_replacement("specific", "OpenAIStructured"))
    print('OpenAIStructured', OpenAIStructured)

    OpenAIDescriptive = (mrr_replacement("specific", "OpenAIDescriptive"))
    print('OpenAIDescriptive', OpenAIDescriptive)

    Meilisearch = (mrr_replacement("specific", "Meilisearch"))
    print('Meilisearch', Meilisearch)

    MeilisearchEmbed = (mrr_replacement("specific", "MeilisearchEmbed"))
    print('MeilisearchEmbed', MeilisearchEmbed)

    GeminiSimple = (mrr_replacement("specific", "GeminiSimple"))
    print('GeminiSimple', GeminiSimple)

    GeminiStructured = (mrr_replacement("specific", "GeminiStructured"))
    print('GeminiStructured', GeminiStructured)

    GeminiDescriptive = (mrr_replacement("specific", "GeminiDescriptive"))
    print('GeminiDescriptive', GeminiDescriptive)

    OpenAIPrompt = (mrr_replacement("specific", "OpenAIPrompt"))
    print('OpenAIPrompt', OpenAIPrompt)

    GeminiPrompt = (mrr_replacement("specific", "GeminiPrompt"))
    print('GeminiPrompt', GeminiPrompt)

    print('------------', 'named', '--------------')

    OpenAISimple = (mrr("named", "OpenAISimple"))
    print('OpenAISimple', OpenAISimple)

    OpenAIStructured = (mrr("named", "OpenAIStructured"))
    print('OpenAIStructured', OpenAIStructured)

    OpenAIDescriptive = (mrr("named", "OpenAIDescriptive"))
    print('OpenAIDescriptive', OpenAIDescriptive)

    Meilisearch = (mrr("named", "Meilisearch"))
    print('Meilisearch', Meilisearch)

    MeilisearchEmbed = (mrr("named", "MeilisearchEmbed"))
    print('MeilisearchEmbed', MeilisearchEmbed)

    GeminiSimple = (mrr("named", "GeminiSimple"))
    print('GeminiSimple', GeminiSimple)

    GeminiStructured = (mrr("named", "GeminiStructured"))
    print('GeminiStructured', GeminiStructured)

    GeminiDescriptive = (mrr("named", "GeminiDescriptive"))
    print('GeminiDescriptive', GeminiDescriptive)

    OpenAIPrompt = (mrr("named", "OpenAIPrompt"))
    print('OpenAIPrompt', OpenAIPrompt)

    GeminiPrompt = (mrr("named", "GeminiPrompt"))
    print('GeminiPrompt', GeminiPrompt)

    print('------------------------------------------')

    # print('OpenAISimpleSum', OpenAISimpleSum / 4)
    # print('OpenAIStructuredSum', OpenAIStructuredSum /4)
    # print('OpenAIDescriptiveSum', OpenAIDescriptiveSum / 4)
    #
    # print('MeilisearchSum', MeilisearchSum / 4)
    # print('MeilisearchEmbedSum', MeilisearchEmbedSum / 4)
    #
    # print('GeminiSimpleSum', GeminiSimpleSum / 4)
    # print('GeminiStructuredSum', GeminiStructuredSum / 4)
    # print('GeminiDescriptiveSum', GeminiDescriptiveSum / 4)
    #
    # print('OpenAIPromptSum', OpenAIPromptSum / 4)
    # print('GeminiPromptSum', GeminiPromptSum / 4)

# score_summary()
# wilk(None, "s5", components, "score_summary.csv") # izjema pri secificnih s5_replace

print("-------------- Summary significance ndcg5  --------------")

wilk(["simple","named","complex"], "ndcg5", component_a , component_b, "score_summary.csv")

print("-------------- Summary significance mrr  --------------")

wilk("specific", "rr_replace", component_a , component_b, "score_summary.csv")