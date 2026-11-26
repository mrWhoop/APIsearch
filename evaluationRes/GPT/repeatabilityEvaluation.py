import pymongo
from pymongo import MongoClient
from pymongo.errors import OperationFailure
from pathlib import Path
import json
from validationUtility import validateMongoQuery
from itertools import combinations
from collections import Counter

import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.environ['MONGO_URI'])
db = client["api"]
collection = db["apis"]

complex = Path("complex")
malicious = Path("malicious")
named = Path("named")
simple = Path("simple")
specific = Path("specific")

INVALID = 0

def normalize_query(query):
    return json.dumps(
        query,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False
    )


def deviation_from_mode(queries):

    if not queries:
        return None

    normalized = [normalize_query(q) for q in queries]
    frequencies = Counter(normalized)

    mode_frequency = max(frequencies.values())

    return (len(normalized) - mode_frequency) / len(normalized)

def jaccard_similarity(results_a, results_b):
    if results_a is None or results_b is None:
        return None

    a = set(results_a)
    b = set(results_b)

    union = a | b
    return len(a & b) / len(union) if union else 1.0

Jaccard_complex = 0
Mode_complex = 0
for file in complex.iterdir():

    if file.is_file():
        try:
            data = json.loads(file.read_text(encoding="utf-8"))
            queries = data["responses"]
            query_results = []
            query_modes = []
            for query in queries:
                try:
                    mongoQuery = json.loads(query)
                except json.JSONDecodeError as e:
                    query_results.append(None)
                    query_modes.append("INVALID")
                    INVALID += 1
                    continue
                if not validateMongoQuery(mongoQuery):
                    query_results.append(None)
                    query_modes.append("INVALID")
                    INVALID += 1
                    continue
                try:
                    apis = collection.find(mongoQuery, {"_id": 1})
                    result_ids = [doc["_id"] for doc in apis]
                    query_results.append(result_ids)
                except pymongo.errors.OperationFailure as e:
                    query_results.append(None)
                    query_modes.append("INVALID")
                    INVALID += 1
                    continue

                query_modes.append(mongoQuery)

            deviation = deviation_from_mode(query_modes)
            Mode_complex = Mode_complex + deviation

            scores = [
                jaccard_similarity(a, b)
                for a, b in combinations(query_results, 2)
            ]

            valid_scores = [score for score in scores if score is not None]

            mean_jaccard = (
                sum(valid_scores) / len(valid_scores)
                if valid_scores else None
            )

            valid_count = sum(r is not None for r in query_results)

            execution_success_rate = (
                valid_count / len(query_results)
                if query_results else 0.0
            )

            # print(f"{file.name}:")
            # print(f"  Mean Jaccard: {mean_jaccard}")
            # print(f"  Valid queries: {valid_count}/{len(query_results)}")
            # print(f"  Execution success rate: {execution_success_rate:.2%}")
            # print(f"  Valid comparisons: {len(valid_scores)}/"
            #       f"{len(scores)}")

            Jaccard_complex = Jaccard_complex + mean_jaccard

        except json.JSONDecodeError as e:
            print(f"Error decoding: {file.name}: {e}")

print("Mode complex: ", Mode_complex/40,  "Jaccard complex: ", Jaccard_complex/40)

Jaccard_named = 0
Mode_named = 0
for file in named.iterdir():

    if file.is_file():
        try:
            data = json.loads(file.read_text(encoding="utf-8"))
            queries = data["responses"]
            query_results = []
            query_modes = []
            for query in queries:
                try:
                    mongoQuery = json.loads(query)
                except json.JSONDecodeError as e:
                    query_results.append(None)
                    query_modes.append("INVALID")
                    INVALID += 1
                    continue
                if not validateMongoQuery(mongoQuery):
                    query_results.append(None)
                    query_modes.append("INVALID")
                    INVALID += 1
                    continue
                try:
                    apis = collection.find(mongoQuery, {"_id": 1})
                    result_ids = [doc["_id"] for doc in apis]
                    query_results.append(result_ids)
                except pymongo.errors.OperationFailure as e:
                    query_results.append(None)
                    query_modes.append("INVALID")
                    INVALID += 1
                    continue

                query_modes.append(mongoQuery)

            deviation = deviation_from_mode(query_modes)
            Mode_named = Mode_named + deviation

            scores = [
                jaccard_similarity(a, b)
                for a, b in combinations(query_results, 2)
            ]

            valid_scores = [score for score in scores if score is not None]

            mean_jaccard = (
                sum(valid_scores) / len(valid_scores)
                if valid_scores else None
            )

            valid_count = sum(r is not None for r in query_results)

            execution_success_rate = (
                valid_count / len(query_results)
                if query_results else 0.0
            )

            # print(f"{file.name}:")
            # print(f"  Mean Jaccard: {mean_jaccard}")
            # print(f"  Valid queries: {valid_count}/{len(query_results)}")
            # print(f"  Execution success rate: {execution_success_rate:.2%}")
            # print(f"  Valid comparisons: {len(valid_scores)}/"
            #       f"{len(scores)}")

            Jaccard_named = Jaccard_named + mean_jaccard

        except json.JSONDecodeError as e:
            print(f"Error decoding: {file.name}: {e}")

print("Mode named: ", Mode_named/40, 'Jaccard named:', Jaccard_named/40)

Jaccard_simple = 0
Mode_simple = 0
for file in simple.iterdir():

    if file.is_file():
        try:
            data = json.loads(file.read_text(encoding="utf-8"))
            queries = data["responses"]
            query_results = []
            query_modes = []
            for query in queries:
                try:
                    mongoQuery = json.loads(query)
                except json.JSONDecodeError as e:
                    query_results.append(None)
                    query_modes.append("INVALID")
                    INVALID += 1
                    continue
                if not validateMongoQuery(mongoQuery):
                    query_results.append(None)
                    query_modes.append("INVALID")
                    INVALID += 1
                    continue
                try:
                    apis = collection.find(mongoQuery, {"_id": 1})
                    result_ids = [doc["_id"] for doc in apis]
                    query_results.append(result_ids)
                except pymongo.errors.OperationFailure as e:
                    query_results.append(None)
                    query_modes.append("INVALID")
                    INVALID += 1
                    continue

                query_modes.append(mongoQuery)

            deviation = deviation_from_mode(query_modes)
            Mode_simple = Mode_simple + deviation

            scores = [
                jaccard_similarity(a, b)
                for a, b in combinations(query_results, 2)
            ]

            valid_scores = [score for score in scores if score is not None]

            mean_jaccard = (
                sum(valid_scores) / len(valid_scores)
                if valid_scores else None
            )

            valid_count = sum(r is not None for r in query_results)

            execution_success_rate = (
                valid_count / len(query_results)
                if query_results else 0.0
            )

            # print(f"{file.name}:")
            # print(f"  Mean Jaccard: {mean_jaccard}")
            # print(f"  Valid queries: {valid_count}/{len(query_results)}")
            # print(f"  Execution success rate: {execution_success_rate:.2%}")
            # print(f"  Valid comparisons: {len(valid_scores)}/"
            #       f"{len(scores)}")

            Jaccard_simple = Jaccard_simple + mean_jaccard

        except json.JSONDecodeError as e:
            print(f"Error decoding: {file.name}: {e}")

print("Mode simple: ", Mode_simple/40, 'Jaccard_simple: ', Jaccard_simple/40)

Jaccard_specific = 0
Mode_specific = 0
for file in specific.iterdir():

    if file.is_file():
        try:
            data = json.loads(file.read_text(encoding="utf-8"))
            queries = data["responses"]
            query_results = []
            query_modes = []
            for query in queries:
                try:
                    mongoQuery = json.loads(query)
                except json.JSONDecodeError as e:
                    query_results.append(None)
                    query_modes.append("INVALID")
                    INVALID += 1
                    continue
                if not validateMongoQuery(mongoQuery):
                    query_results.append(None)
                    query_modes.append("INVALID")
                    INVALID += 1
                    continue
                try:
                    apis = collection.find(mongoQuery, {"_id": 1})
                    result_ids = [doc["_id"] for doc in apis]
                    query_results.append(result_ids)
                except pymongo.errors.OperationFailure as e:
                    query_results.append(None)
                    query_modes.append("INVALID")
                    INVALID += 1
                    continue

                query_modes.append(mongoQuery)

            deviation = deviation_from_mode(query_modes)
            Mode_specific = Mode_specific + deviation

            scores = [
                jaccard_similarity(a, b)
                for a, b in combinations(query_results, 2)
            ]

            valid_scores = [score for score in scores if score is not None]

            mean_jaccard = (
                sum(valid_scores) / len(valid_scores)
                if valid_scores else None
            )

            valid_count = sum(r is not None for r in query_results)

            execution_success_rate = (
                valid_count / len(query_results)
                if query_results else 0.0
            )

            # print(f"{file.name}:")
            # print(f"  Mean Jaccard: {mean_jaccard}")
            # print(f"  Valid queries: {valid_count}/{len(query_results)}")
            # print(f"  Execution success rate: {execution_success_rate:.2%}")
            # print(f"  Valid comparisons: {len(valid_scores)}/"
            #       f"{len(scores)}")

            Jaccard_specific = Jaccard_specific + mean_jaccard

        except json.JSONDecodeError as e:
            print(f"Error decoding: {file.name}: {e}")

print("Mode specific: ", Mode_specific/40, 'Jaccard specific: ', Jaccard_specific/40)
print("INVALID queries: ", INVALID)