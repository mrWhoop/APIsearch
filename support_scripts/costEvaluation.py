from sys import implementation

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
collection = db["token"]

print("MeiliSearchHybrid")
token = collection.find({"implementation": "MeiliSearchHybrid"}, {"_id": 0, "totalTokens": 1, "inputTokens": 1, "outputTokens": 1})
tokens = [doc["totalTokens"] for doc in token if doc.get("totalTokens") is not None]
median = np.median(tokens)
average = np.mean(tokens)
p95 = np.percentile(tokens, 95)

print(f"Median: {median:.3f}")
print(f"Average: {average:.3f}")
print(f"P95: {p95:.3f}")
print(f"Number of measurements: {len(tokens)}")
print("-------------------------------------")

print("text-embedding-3-large")
token = collection.find({"model": "text-embedding-3-large"}, {"_id": 0, "totalTokens": 1})
tokens = [doc["totalTokens"] for doc in token if doc.get("totalTokens") is not None]
median = np.median(tokens)
average = np.mean(tokens)
p95 = np.percentile(tokens, 95)

print(f"Median: {median:.3f}")
print(f"Average: {average:.3f}")
print(f"P95: {p95:.3f}")
print(f"Number of measurements: {len(tokens)}")
print("-------------------------------------")

print("gemini-embedding-001")
token = collection.find({"model": "gemini-embedding-001"}, {"_id": 0, "totalTokens": 1, "inputTokens": 1})
tokens = [doc["totalTokens"] for doc in token if doc.get("totalTokens") is not None]
median = np.median(tokens)
average = np.mean(tokens)
p95 = np.percentile(tokens, 95)

print(f"Median: {median:.3f}")
print(f"Average: {average:.3f}")
print(f"P95: {p95:.3f}")
print(f"Number of measurements: {len(tokens)}")
print("-------------------------------------")

print("GPTPrompt")
token = list(collection.find({"implementation": "GPTPrompt"}, {"_id": 0, "totalTokens": 1, "inputTokens": 1, "outputTokens": 1}))
tokens = [doc["totalTokens"] for doc in token]
inTokens = [doc["inputTokens"] for doc in token]
outTokens = [doc["outputTokens"] for doc in token]
median = np.median(tokens)
medianIn = np.median(inTokens)
medianOut = np.median(outTokens)
average = np.mean(tokens)
p95 = np.percentile(tokens, 95)
cost = (medianIn * 0.1)/1000 + (medianOut * 0.2)/1000
print(f"Median: {median:.3f}")
print(f"MedianIn: {medianIn:.3f}")
print(f"MedianOut: {medianOut:.3f}")
print(f"Average: {average:.3f}")
print(f"P95: {p95:.3f}")
print(f"Number of measurements: {len(tokens)}")
print(f"cost: {cost:.3f}")
print("-------------------------------------")

print("GeminiPrompt")
token = list(collection.find({"implementation": "GeminiPrompt"}, {"_id": 0, "totalTokens": 1, "inputTokens": 1, "outputTokens": 1, "thinkingTokens": 1}))
tokens = [doc["totalTokens"] for doc in token]
inTokens = [doc["inputTokens"] for doc in token]
outTokens = [doc["outputTokens"] for doc in token]
thinkTokens = [doc["thinkingTokens"] for doc in token]
combined = [a + b for a, b in zip(outTokens, thinkTokens)]
median = np.median(tokens)
medianIn = np.median(inTokens)
medianOut = np.median(combined)
average = np.mean(tokens)
p95 = np.percentile(tokens, 95)
cost = (0.75 * medianIn)/1000 + (3.75 * medianOut)/1000
print(f"Median: {median:.3f}")
print(f"MedianIn: {medianIn:.3f}")
print(f"MedianOut: {medianOut:.3f}")
print(f"Average: {average:.3f}")
print(f"P95: {p95:.3f}")
print(f"Number of measurements: {len(tokens)}")
print(f"cost: {cost:.3f}")
print("-------------------------------------")
print("-------------------------------------")

print("GeminiComparePrompt")
token = list(collection.find({"implementation": "GeminiComparePrompt"}, {"_id": 0, "totalTokens": 1, "inputTokens": 1, "outputTokens": 1, "thinkingTokens": 1}))
tokens = [doc["totalTokens"] for doc in token]
inTokens = [doc["inputTokens"] for doc in token]
outTokens = [doc["outputTokens"] for doc in token]
thinkTokens = [doc["thinkingTokens"] for doc in token]
combined = [a + b for a, b in zip(outTokens, thinkTokens)]
median = np.median(tokens)
medianIn = np.median(inTokens)
medianOut = np.median(combined)
average = np.mean(tokens)
p95 = np.percentile(tokens, 95)
cost = (0.75 * medianIn)/1000 + (3.75 * medianOut)/1000
print(f"Median: {median:.3f}")
print(f"MedianIn: {medianIn:.3f}")
print(f"MedianOut: {medianOut:.3f}")
print(f"Average: {average:.3f}")
print(f"P95: {p95:.3f}")
print(f"Number of measurements: {len(tokens)}")
print(f"cost: {cost:.3f}")
print("-------------------------------------")

print("GPTComparePrompt")
token = list(collection.find({"implementation": "GPTComparePrompt"}, {"_id": 0, "totalTokens": 1, "inputTokens": 1, "outputTokens": 1}))
tokens = [doc["totalTokens"] for doc in token]
inTokens = [doc["inputTokens"] for doc in token]
outTokens = [doc["outputTokens"] for doc in token]
median = np.median(tokens)
medianIn = np.median(inTokens)
medianOut = np.median(outTokens)
average = np.mean(tokens)
p95 = np.percentile(tokens, 95)
cost = (medianIn * 0.1)/1000 + (medianOut * 0.2)/1000
print(f"Median: {median:.3f}")
print(f"MedianIn: {medianIn:.3f}")
print(f"MedianOut: {medianOut:.3f}")
print(f"Average: {average:.3f}")
print(f"P95: {p95:.3f}")
print(f"Number of measurements: {len(tokens)}")
print(f"cost: {cost:.3f}")
models = set()
implementation = set()
time = collection.find({})
for t in time:
    models.add(t["model"])
    implementation.add(t["implementation"])
print(models)
print(implementation)
