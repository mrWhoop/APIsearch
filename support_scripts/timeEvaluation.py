import pymongo
from pymongo import MongoClient
from pymongo.errors import OperationFailure
from pathlib import Path
import json
import chromadb
import os
from dotenv import load_dotenv
import numpy as np

load_dotenv()

client = MongoClient(os.environ['MONGO_READWRITE_URI'])
db = client["api"]
collection = db["time"]

time = collection.find({})
models = set()
implementation = set()

print("MeiliSearchBasic")
time = collection.find({"implementation": "MeiliSearchBasic"}, {"_id": 0, "deltaTime": 1})
times = [doc["deltaTime"] for doc in time if doc.get("deltaTime") is not None]
median = np.median(times)
average = np.mean(times)
p95 = np.percentile(times, 95)

print(f"Median: {median:.3f}")
print(f"Mean: {average:.3f}")
print(f"P95: {p95:.3f}")
print(f"Number of measurements: {len(times)}")
print("-------------------------------------")

print("MeiliSearchHybrid")
time = collection.find({"implementation": "MeiliSearchHybrid"}, {"_id": 0, "deltaTime": 1})
times = [doc["deltaTime"] for doc in time if doc.get("deltaTime") is not None]
median = np.median(times)
average = np.mean(times)
p95 = np.percentile(times, 95)

print(f"Median: {median:.3f}")
print(f"Mean: {average:.3f}")
print(f"P95: {p95:.3f}")
print(f"Number of measurements: {len(times)}")
print("-------------------------------------")

print("text-embedding-3-large")
time = collection.find({"model": "text-embedding-3-large"}, {"_id": 0, "deltaTime": 1})
times = [doc["deltaTime"] for doc in time if doc.get("deltaTime") is not None]
median = np.median(times)
average = np.mean(times)
p95 = np.percentile(times, 95)

print(f"Median: {median:.3f}")
print(f"Mean: {average:.3f}")
print(f"P95: {p95:.3f}")
print(f"Number of measurements: {len(times)}")
print("-------------------------------------")

print("gemini-embedding-001")
time = collection.find({"model": "gemini-embedding-001"}, {"_id": 0, "deltaTime": 1})
times = [doc["deltaTime"] for doc in time if doc.get("deltaTime") is not None]
median = np.median(times)
average = np.mean(times)
p95 = np.percentile(times, 95)

print(f"Median: {median:.3f}")
print(f"Mean: {average:.3f}")
print(f"P95: {p95:.3f}")
print(f"Number of measurements: {len(times)}")
print("-------------------------------------")

print("GPTPrompt")
time = collection.find({"implementation": "GPTPrompt"}, {"_id": 0, "deltaTime": 1})
times = [doc["deltaTime"] for doc in time if doc.get("deltaTime") is not None]
median = np.median(times)
average = np.mean(times)
p95 = np.percentile(times, 95)

print(f"Median: {median:.3f}")
print(f"Mean: {average:.3f}")
print(f"P95: {p95:.3f}")
print(f"Number of measurements: {len(times)}")
print("-------------------------------------")

print("GeminiPrompt")
time = collection.find({"implementation": "GeminiPrompt"}, {"_id": 0, "deltaTime": 1})
times = [doc["deltaTime"] for doc in time if doc.get("deltaTime") is not None]
median = np.median(times)
average = np.mean(times)
p95 = np.percentile(times, 95)

print(f"Median: {median:.3f}")
print(f"Mean: {average:.3f}")
print(f"P95: {p95:.3f}")
print(f"Number of measurements: {len(times)}")
print("-------------------------------------")
print("-------------------------------------")

print("GeminiComparePrompt")
time = collection.find({"implementation": "GeminiComparePrompt"}, {"_id": 0, "deltaTime": 1})
times = [doc["deltaTime"] for doc in time if doc.get("deltaTime") is not None]
median = np.median(times)
average = np.mean(times)
p95 = np.percentile(times, 95)

print(f"Median: {median:.3f}")
print(f"Mean: {average:.3f}")
print(f"P95: {p95:.3f}")
print(f"Number of measurements: {len(times)}")
print("-------------------------------------")

print("GPTComparePrompt")
time = collection.find({"implementation": "GPTComparePrompt"}, {"_id": 0, "deltaTime": 1})
times = [doc["deltaTime"] for doc in time if doc.get("deltaTime") is not None]
median = np.median(times)
average = np.mean(times)
p95 = np.percentile(times, 95)

print(f"Median: {median:.3f}")
print(f"Mean: {average:.3f}")
print(f"P95: {p95:.3f}")
print(f"Number of measurements: {len(times)}")

time = collection.find({})
for t in time:
    models.add(t["model"])
    implementation.add(t["implementation"])
print(models)
print(implementation)

