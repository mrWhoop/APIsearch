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

import numpy as np

load_dotenv()

client = MongoClient(os.environ['MONGO_READWRITE_URI'])
db = client["api"]
# collection = db["comparisonEvaluation"]
collection = db["simulatedComparisonEvaluation"]


def evaluateComparisonComponent(model):
    evaluations = collection.find({"model": model})

    fluency = 0.0
    groundness = 0.0
    faithfulness = 0.0

    for evaluation in evaluations:
        grades = evaluation.get("grades")

        fluency = fluency + grades["fluency"]
        groundness = groundness + grades["groundness"]
        faithfulness = faithfulness + grades["faithfulness"]

    # Avtor
    # print(model, 'fluency: ', fluency/40, 'groundness: ', groundness/40, 'faithfulness: ', faithfulness/40)

    # Ocenjevalec
    print(model, 'fluency: ', fluency / 10, 'groundness: ', groundness / 10, 'faithfulness: ', faithfulness / 10)

evaluateComparisonComponent('GPT')
evaluateComparisonComponent('Gemini')

def wilk(metric, models, file_name):

    scores = {}

    for model in models:

        documents = collection.find(
            {"model": model},
            {
                "_id": 0,
                "query": 1,
                f"grades.{metric}": 1
            }
            ).sort("query", 1)

        scores[model] = {
            doc["query"]: doc["grades"][metric]
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

wilk('fluency', ['GPT', 'Gemini'], 'comparison_fluency.csv')
wilk('faithfulness',  ['GPT', 'Gemini'], 'comparison_faithfulness.csv')
wilk('groundness',  ['GPT', 'Gemini'], 'comparison_groundness.csv')

