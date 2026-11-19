from sklearn.metrics import cohen_kappa_score
import pymongo
from pymongo import MongoClient
from pymongo.errors import OperationFailure
from pathlib import Path
import json
import chromadb
from statistics import mean

import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.environ['MONGO_READWRITE_URI'])
db = client["api"]
author = db["searchEvaluation"]
evaluator = db["simulatedSearchEvaluation"]

evaluatorScores = evaluator.find({})

def get_ratings(accepted, rejected):
    ratings = {}

    for api in accepted or []:
        ratings[api["id"]] = 1

    for api in rejected or []:
        ratings[api["id"]] = 0

    return ratings

allAuthor = []
allEvaluator = []

print('-------------------- search component -------------------------')

for eS in evaluatorScores:
    authorCounterpart = author.find_one({"query": eS.get("query"), "component": eS.get("component")})

    authorAccepted = authorCounterpart.get("accepted")
    authorRejected = authorCounterpart.get("rejected")

    evaluatorAccepted = eS.get("accepted")
    evaluatorRejected = eS.get("rejected")

    if authorCounterpart is None:
        print("Error: no author evaluation found.")
        exit()

    authorRatings = get_ratings(authorAccepted, authorRejected)
    evaluatorRatings = get_ratings(evaluatorAccepted, evaluatorRejected)

    if set(authorRatings) != set(evaluatorRatings):
        print(f"Different API pools for query: {eS.get('query')}")
        exit()

    commonIds = set(authorRatings) & set(evaluatorRatings)

    for apiId in commonIds:
        allAuthor.append(authorRatings[apiId])
        allEvaluator.append(evaluatorRatings[apiId])

if allAuthor:
    kappa = cohen_kappa_score(allAuthor, allEvaluator)

    agreement = sum(
        a == b for a, b in zip(allAuthor, allEvaluator)
    ) / len(allAuthor)

    print(f"Cohen's Kappa: {kappa:.4f}")
    print(f"Agreement: {agreement:.2%}")
    print(f"Compared API pairs: {len(allAuthor)}")
else:
    print("No matching API evaluations found.")

print('-------------------- comparison component -------------------------')


from statistics import mean
from sklearn.metrics import cohen_kappa_score, confusion_matrix

authorComparison = db["comparisonEvaluation"]
evaluatorComparison = db["simulatedComparisonEvaluation"]

criteria = ["fluency", "groundness", "faithfulness"]

allScores = {}


scores = {
    criterion: {"author": [], "evaluator": []}
    for criterion in criteria
}

evaluatorComparisonScores = evaluatorComparison.find({})

for eCS in evaluatorComparisonScores:
    authorCounterpart = authorComparison.find_one({
        "query": eCS.get("query"),
        "model": eCS.get("model")
    })

    if not authorCounterpart:
        print(f"Missing counterpart: {eCS.get('query')}")
        continue

    authorGrades = authorCounterpart.get("grades", {})
    evaluatorGrades = eCS.get("grades", {})

    for criterion in criteria:
        authorGrade = authorGrades.get(criterion)
        evaluatorGrade = evaluatorGrades.get(criterion)

        if authorGrade is None or evaluatorGrade is None:
            continue

        scores[criterion]["author"].append(authorGrade)
        scores[criterion]["evaluator"].append(evaluatorGrade)

for criterion in criteria:
    authorGrades = scores[criterion]["author"]
    evaluatorGrades = scores[criterion]["evaluator"]

    n = len(authorGrades)

    if n == 0:
        continue

    differences = [
        abs(a - b)
        for a, b in zip(authorGrades, evaluatorGrades)
    ]

    exactAgreement = sum(
        a == b for a, b in zip(authorGrades, evaluatorGrades)
    ) / n

    withinOne = sum(d <= 1 for d in differences) / n
    mad = mean(differences)

    kappa = cohen_kappa_score(
        authorGrades,
        evaluatorGrades,
        labels=[0, 1, 2, 3, 4],
        weights="quadratic"
    )

    meanDifference = mean(
        b - a
        for a, b in zip(authorGrades, evaluatorGrades)
    )

    print(
        f"{criterion}: "
        f"Exact agreement={exactAgreement:.3f}, "
        f"Within 1={withinOne:.3f}, "
        f"MAD={mad:.3f}, "
        f"Mean difference={meanDifference:+.3f}, "
        f"Weighted kappa={kappa:.3f}, "
        f"n={n}"
    )

    # print(confusion_matrix(
    #     authorGrades,
    #     evaluatorGrades,
    #     labels=[0, 1, 2, 3, 4]
    # ))
