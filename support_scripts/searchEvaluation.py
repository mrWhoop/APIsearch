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

components = [
        "OpenAISimple",
        "OpenAIStructured",
        "OpenAIDescriptive",
        "Meilisearch",
        "MeilisearchEmbed",
        "GeminiSimple",
        "GeminiStructured",
        "GeminiDescriptive",
        "OpenAIPrompt",
        "GeminiPrompt",
    ]


import itertools
import numpy as np
import pandas as pd

from scipy.stats import wilcoxon, bootstrap
from statsmodels.stats.multitest import multipletests



def wilk(queryType, metric, components, file_name):

    scores = {}

    for component in components:
        if queryType is None:
            documents = collection.aggregate([
                {
                    "$match": {
                        "component": component
                    }
                },
                {
                    "$project": {
                        "_id": 0,
                        "query": 1,
                        "s5": {
                            "$cond": [
                                {"$eq": ["$queryType", "specific"]},
                                "$s5_replace",
                                "$s5"
                            ]
                        }
                    }
                },
                {
                    "$sort": {"query": 1}
                }
            ])
        else:
            documents = collection.find(
                {
                    "queryType": queryType,
                    "component": component
                },
                {
                    "_id": 0,
                    "query": 1,
                    metric: 1
                }
            ).sort("query", 1)

        scores[component] = {
            doc["query"]: doc[metric]
            for doc in documents
        }

    # bootstrap: difference between means A - B
    def mean_difference(a, b, axis=-1):
        return np.mean(a - b, axis=axis)

    results = []

    for system_a, system_b in itertools.combinations(scores, 2):

        common_queries = sorted(
            set(scores[system_a]) & set(scores[system_b])
        )

        a = np.asarray(
            [scores[system_a][q] for q in common_queries],
            dtype=float
        )
        b = np.asarray(
            [scores[system_b][q] for q in common_queries],
            dtype=float
        )

        if len(a) == 0:
            continue

        if not np.isfinite(a).all() or not np.isfinite(b).all():
            raise ValueError(
                f"Non-finite scores for {system_a} and {system_b}"
            )

        mean_a = np.mean(a)
        mean_b = np.mean(b)
        observed_difference = np.mean(a - b)

        # Wilcoxon signed-rank test
        if np.all(a == b):
            statistic, p_value = 0.0, 1.0
        else:
            test = wilcoxon(a, b, alternative="two-sided")
            statistic = test.statistic
            p_value = test.pvalue

        # Paired bootstrap 95% confidence interval
        boot = bootstrap(
            (a, b),
            mean_difference,
            paired=True,
            vectorized=True,
            n_resamples=50_000,
            confidence_level=0.95,
            method="percentile",
            rng=np.random.default_rng(42)
        )

        ci_lower = boot.confidence_interval.low
        ci_upper = boot.confidence_interval.high

        results.append({
            "component_a": system_a,
            "component_b": system_b,
            "n_queries": len(common_queries),
            "mean_a": mean_a,
            "mean_b": mean_b,
            "mean_difference": observed_difference,
            "ci_lower": ci_lower,
            "ci_upper": ci_upper,
            "bootstrap_significant": ci_lower > 0 or ci_upper < 0,
            "statistic": statistic,
            "p_value": p_value,
            "p_significant": p_value < 0.05
        })

    df = pd.DataFrame(results)

    if not df.empty:

        # Holm correction across all pairwise comparisons
        df["p_adjusted"] = multipletests(
            df["p_value"],
            method="holm"
        )[1]

        # Use adjusted p-values for statistical significance
        df["significant"] = df["p_adjusted"] <= 0.05

        print(
            df.sort_values("significant").to_string(index=False)
        )

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

    # print(component, sum(scores) / len(scores) if scores else 0.0, len(scores))

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

        # Ideal DCG@5: relevant results ranked first
        relevant_count = min(
            sum(relevance.values()),
            5
        )

        idcg = sum(
            1 / math.log2(position + 1)
            for position in range(1, relevant_count + 1)
        )

        # nDCG@5

        score = dcg / idcg if idcg > 0 else 0.0
        scores.append(score)

        collection.update_one(
            {"_id": evaluation["_id"]},
            {"$set": {"ndcg5": score}}
        )

    # print(component, sum(scores) / len(scores) if scores else 0.0)
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
#
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
#
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
#
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
#
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
#
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
#
# ndcg_at_5("complex", "OpenAIPrompt")
# ndcg_at_5("complex", "GeminiPrompt")

print("-------------- SIMPLE score --------------" )
# score_eval("simple")
# wilk("simple", "precision5", components, "enostavne_poizvedbe_PrecisionRate5.csv")
# wilk("simple", "ndcg5", components, "enostavne_poizvedbe_ndcgRate5.csv")
# wilk("simple", "s5", components, "enostavne_poizvedbe_S5.csv")

print("-------------- NAMED score --------------" )
# score_eval("named")
# wilk("named", "precision5", components, "poimenske_poizvedbe_PrecisionRate5.csv")
# wilk("named", "ndcg5", components, "poimenske_poizvedbe_ndcgRate5.csv")
# wilk("named", "s5", components, "poimenske_poizvedbe_s5.csv")

print("-------------- COMPLEX score --------------" )
# score_eval("complex")
# wilk("complex", "precision5", components, "sestavljene_poizvedbe_PrecisionRate5.csv")
# wilk("complex", "ndcg5", components, "sestavljene_poizvedbe_ndcgRate5.csv")
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


    # print(component, sum(reciprocal_ranks) / len(reciprocal_ranks) if reciprocal_ranks else 0.0)
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
#
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
#
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
#
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

    # print(component, hit / total if total else 0.0)
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
#
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

print("-------------- SPECIFIC score replacement --------------")
# score_eval_specific_replacement("specific")

#wilk("specific", "rr_replace", components, "specificne_poizvedbe_mrr.csv")
#wilk("specific", "hit_replace", components, "specificne_poizvedbe_hit1.csv")
#wilk("specific", "s5_replace", components, "specificne_poizvedbe_s5.csv")

print("-------------- Score@5 summary --------------")

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

        OpenAISimple = (precision_at_5(queryType, "OpenAISimple") + ndcg_at_5(queryType, "OpenAISimple")) / 2
        OpenAISimpleSum = OpenAISimpleSum + OpenAISimple
        print('OpenAISimple', OpenAISimple)

        OpenAIStructured = (precision_at_5(queryType, "OpenAIStructured") + ndcg_at_5(queryType, "OpenAIStructured")) / 2
        OpenAIStructuredSum = OpenAIStructuredSum + OpenAIStructured
        print('OpenAIStructured', OpenAIStructured)

        OpenAIDescriptive = (precision_at_5(queryType, "OpenAIDescriptive") + ndcg_at_5(queryType, "OpenAIDescriptive")) / 2
        OpenAIDescriptiveSum = OpenAIDescriptiveSum + OpenAIDescriptive
        print('OpenAIDescriptive', OpenAIDescriptive)

        Meilisearch = (precision_at_5(queryType, "Meilisearch") + ndcg_at_5(queryType, "Meilisearch")) / 2
        MeilisearchSum = MeilisearchSum + Meilisearch
        print('Meilisearch', Meilisearch)

        MeilisearchEmbed = (precision_at_5(queryType, "MeilisearchEmbed") + ndcg_at_5(queryType, "MeilisearchEmbed")) / 2
        MeilisearchEmbedSum = MeilisearchEmbedSum + MeilisearchEmbed
        print('MeilisearchEmbed', MeilisearchEmbed)

        GeminiSimple = (precision_at_5(queryType, "GeminiSimple") + ndcg_at_5(queryType, "GeminiSimple")) / 2
        GeminiSimpleSum = GeminiSimpleSum + GeminiSimple
        print('GeminiSimple', GeminiSimple)

        GeminiStructured = (precision_at_5(queryType, "GeminiStructured") + ndcg_at_5(queryType, "GeminiStructured")) / 2
        GeminiStructuredSum = GeminiStructuredSum + GeminiStructured
        print('GeminiStructured', GeminiStructured)

        GeminiDescriptive = (precision_at_5(queryType, "GeminiDescriptive") + ndcg_at_5(queryType, "GeminiDescriptive")) / 2
        GeminiDescriptiveSum = GeminiDescriptiveSum + GeminiDescriptive
        print('GeminiDescriptive', GeminiDescriptive)

        OpenAIPrompt = (precision_at_5(queryType, "OpenAIPrompt") + ndcg_at_5(queryType, "OpenAIPrompt")) / 2
        OpenAIPromptSum = OpenAIPromptSum + OpenAIPrompt
        print('OpenAIPrompt', OpenAIPrompt)

        GeminiPrompt = (precision_at_5(queryType, "GeminiPrompt") + ndcg_at_5(queryType, "GeminiPrompt")) / 2
        GeminiPromptSum = GeminiPromptSum + GeminiPrompt
        print('GeminiPrompt', GeminiPrompt)

    print('------------', 'specific', '--------------')

    OpenAISimple = (hit_at_1_replacement("specific", "OpenAISimple") + mrr_replacement("specific", "OpenAISimple")) / 2
    OpenAISimpleSum = OpenAISimpleSum + OpenAISimple
    print('OpenAISimple', OpenAISimple)

    OpenAIStructured = (hit_at_1_replacement("specific", "OpenAIStructured") + mrr_replacement("specific", "OpenAIStructured")) / 2
    OpenAIStructuredSum = OpenAIStructuredSum + OpenAIStructured
    print('OpenAIStructured', OpenAIStructured)

    OpenAIDescriptive = (hit_at_1_replacement("specific", "OpenAIDescriptive") + mrr_replacement("specific", "OpenAIDescriptive")) / 2
    OpenAIDescriptiveSum = OpenAIDescriptiveSum + OpenAIDescriptive
    print('OpenAIDescriptive', OpenAIDescriptive)

    Meilisearch = (hit_at_1_replacement("specific", "Meilisearch") + mrr_replacement("specific", "Meilisearch")) / 2
    MeilisearchSum = MeilisearchSum + Meilisearch
    print('Meilisearch', Meilisearch)

    MeilisearchEmbed = (hit_at_1_replacement("specific", "MeilisearchEmbed") + mrr_replacement("specific", "MeilisearchEmbed")) / 2
    MeilisearchEmbedSum = MeilisearchEmbedSum + MeilisearchEmbed
    print('MeilisearchEmbed', MeilisearchEmbed)

    GeminiSimple = (hit_at_1_replacement("specific", "GeminiSimple") + mrr_replacement("specific", "GeminiSimple")) / 2
    GeminiSimpleSum = GeminiSimpleSum + GeminiSimple
    print('GeminiSimple', GeminiSimple)

    GeminiStructured = (hit_at_1_replacement("specific", "GeminiStructured") + mrr_replacement("specific", "GeminiStructured")) / 2
    GeminiStructuredSum = GeminiStructuredSum + GeminiStructured
    print('GeminiStructured', GeminiStructured)

    GeminiDescriptive = (hit_at_1_replacement("specific", "GeminiDescriptive") + mrr_replacement("specific", "GeminiDescriptive")) / 2
    GeminiDescriptiveSum = GeminiDescriptiveSum + GeminiDescriptive
    print('GeminiDescriptive', GeminiDescriptive)

    OpenAIPrompt = (hit_at_1_replacement("specific", "OpenAIPrompt") + mrr_replacement("specific", "OpenAIPrompt")) / 2
    OpenAIPromptSum = OpenAIPromptSum + OpenAIPrompt
    print('OpenAIPrompt', OpenAIPrompt)

    GeminiPrompt = (hit_at_1_replacement("specific", "GeminiPrompt") + mrr_replacement("specific", "GeminiPrompt")) / 2
    GeminiPromptSum = GeminiPromptSum + GeminiPrompt
    print('GeminiPrompt', GeminiPrompt)

    print('------------------------------------------')

    print('OpenAISimpleSum', OpenAISimpleSum / 4)
    print('OpenAIStructuredSum', OpenAIStructuredSum / 4)
    print('OpenAIDescriptiveSum', OpenAIDescriptiveSum / 4)

    print('MeilisearchSum', MeilisearchSum / 4)
    print('MeilisearchEmbedSum', MeilisearchEmbedSum / 4)

    print('GeminiSimpleSum', GeminiSimpleSum / 4)
    print('GeminiStructuredSum', GeminiStructuredSum / 4)
    print('GeminiDescriptiveSum', GeminiDescriptiveSum / 4)

    print('OpenAIPromptSum', OpenAIPromptSum / 4)
    print('GeminiPromptSum', GeminiPromptSum / 4)

score_summary()
#wilk(None, "s5", components, "score_summary.csv") # izjema pri secificnih s5_replace