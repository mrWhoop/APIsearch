# ustvarjeno z uporabo UI

import os
import sys
from collections import defaultdict
from statistics import mean

import pandas as pd
from dotenv import load_dotenv
from irrCAC.raw import CAC
from pymongo import MongoClient
from sklearn.metrics import cohen_kappa_score

load_dotenv()

client = MongoClient(os.environ["MONGO_READWRITE_URI"])
db = client["api"]


# =====================================================================
# Search component
# =====================================================================

author = db["searchEvaluation"]
evaluator = db["simulatedSearchEvaluation"]


def get_ratings(accepted, rejected):
    """{apiId: 1 (accepted) / 0 (rejected)}"""
    ratings = {}
    for api in accepted or []:
        ratings[api["id"]] = 1
    for api in rejected or []:
        ratings[api["id"]] = 0
    return ratings


def print_agreement(label, author_ratings, evaluator_ratings):
    kappa = cohen_kappa_score(author_ratings, evaluator_ratings)
    agreement = sum(
        a == b for a, b in zip(author_ratings, evaluator_ratings)
    ) / len(author_ratings)

    print(f"{label}:")
    print(f"  Cohen's Kappa: {kappa:.4f}")
    print(f"  Agreement: {agreement:.2%}")
    print(f"  Pairs: {len(author_ratings)}")
    print(f"  Share accepted (author): {mean(author_ratings):.2%}")
    print(f"  Share accepted (evaluator): {mean(evaluator_ratings):.2%}")


print("-------------------- search component -------------------------")

# all pairs (query–system–API)
allAuthor = []
allEvaluator = []

# (query, apiId) -> ratings across systems
authorByPair = defaultdict(list)
evaluatorByPair = defaultdict(list)

queries = set()
components = set()

for eS in evaluator.find({}):
    query = eS.get("query")
    component = eS.get("component")

    authorCounterpart = author.find_one({"query": query, "component": component})

    if authorCounterpart is None:
        print(f"Error: no author evaluation found for {query!r} / {component}")
        sys.exit(1)

    authorRatings = get_ratings(
        authorCounterpart.get("accepted"), authorCounterpart.get("rejected")
    )
    evaluatorRatings = get_ratings(eS.get("accepted"), eS.get("rejected"))

    if set(authorRatings) != set(evaluatorRatings):
        print(f"Different API pools for query {query!r} / {component}")
        sys.exit(1)

    queries.add(query)
    components.add(component)

    for apiId in authorRatings:
        allAuthor.append(authorRatings[apiId])
        allEvaluator.append(evaluatorRatings[apiId])

        authorByPair[(query, apiId)].append(authorRatings[apiId])
        evaluatorByPair[(query, apiId)].append(evaluatorRatings[apiId])

if not allAuthor:
    print("No matching API evaluations found.")
else:
    print(f"Queries: {len(queries)}")
    print(f"Systems: {len(components)} {sorted(components)}")
    print()

    # consistency check: same query–API must have the same rating everywhere
    authorInconsistent = [k for k, v in authorByPair.items() if len(set(v)) > 1]
    evaluatorInconsistent = [k for k, v in evaluatorByPair.items() if len(set(v)) > 1]

    print(f"Inconsistent query–API pairs (author): {len(authorInconsistent)}")
    print(f"Inconsistent query–API pairs (evaluator): {len(evaluatorInconsistent)}")
    for k in authorInconsistent[:10]:
        print(f"  author: {k} -> {authorByPair[k]}")
    for k in evaluatorInconsistent[:10]:
        print(f"  evaluator: {k} -> {evaluatorByPair[k]}")
    print()

    # all pairs (each occurrence counted)
    print_agreement("All pairs (query–system–API)", allAuthor, allEvaluator)
    print()

    # unique pairs (each query–API counted once)
    keys = sorted(authorByPair)
    uniqueAuthor = [authorByPair[k][0] for k in keys]
    uniqueEvaluator = [evaluatorByPair[k][0] for k in keys]

    print_agreement("Unique pairs (query–API)", uniqueAuthor, uniqueEvaluator)


# =====================================================================
# Comparison component
# =====================================================================

print()
print("-------------------- comparison component -------------------------")

authorComparison = db["comparisonEvaluation"]
evaluatorComparison = db["simulatedComparisonEvaluation"]

criteria = ["fluency", "groundness", "faithfulness"]
labels = [0, 1, 2, 3, 4]


def gwet_irrcac(author_grades, evaluator_grades, weights="quadratic"):
    ratings = pd.DataFrame({
        "author": author_grades,
        "evaluator": evaluator_grades,
    })
    cac = CAC(ratings, weights=weights, categories=labels)
    return cac.gwet()["est"]


scores = {
    criterion: {"author": [], "evaluator": []}
    for criterion in criteria
}

for eCS in evaluatorComparison.find({}):
    authorCounterpart = authorComparison.find_one({
        "query": eCS.get("query"),
        "model": eCS.get("model"),
    })

    if not authorCounterpart:
        print(f"Missing counterpart: {eCS.get('query')} / {eCS.get('model')}")
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

    differences = [abs(a - b) for a, b in zip(authorGrades, evaluatorGrades)]

    exactAgreement = sum(a == b for a, b in zip(authorGrades, evaluatorGrades)) / n
    withinOne = sum(d <= 1 for d in differences) / n
    mad = mean(differences)
    meanDifference = mean(b - a for a, b in zip(authorGrades, evaluatorGrades))

    kappa = cohen_kappa_score(
        authorGrades,
        evaluatorGrades,
        labels=labels,
        weights="quadratic",
    )

    ac2 = gwet_irrcac(authorGrades, evaluatorGrades, weights="quadratic")
    ac2_low, ac2_high = ac2["confidence_interval"]

    print(
        f"{criterion}: "
        f"Exact agreement={exactAgreement:.3f}, "
        f"Within 1={withinOne:.3f}, "
        f"MAD={mad:.3f}, "
        f"Mean difference={meanDifference:+.3f}, "
        f"Weighted kappa={kappa:.3f}, "
        f"Gwet AC2={ac2['coefficient_value']:.3f} "
        f"[{ac2_low:.3f}, {ac2_high:.3f}], "
        f"n={n}"
    )