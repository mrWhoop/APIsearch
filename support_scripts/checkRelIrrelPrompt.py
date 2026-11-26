from pymongo import MongoClient
import os
from dotenv import load_dotenv




load_dotenv()

client = MongoClient(os.environ['MONGO_READWRITE_URI'])
db = client["api"]
collection = db["searchEvaluation"]

gemini = collection.find({"component": "GeminiPrompt"})

geminiFive = 0
geminiFiveQuery = set()

for g in gemini:
    acc = g.get("accepted", [])
    rec = g.get("rejected", [])

    if len(acc) + len(rec) < 5:
        geminiFive += 1
        geminiFiveQuery.add(g.get("queryType"))

print(geminiFive)
print(geminiFiveQuery)

gpt = collection.find({"component": "OpenAIPrompt"})

GPTFive = 0
GPTFiveQuery = set()

for g in gpt:
    acc = g.get("accepted", [])
    rec = g.get("rejected", [])

    if len(acc) + len(rec) < 5:
        GPTFive += 1
        GPTFiveQuery.add(g.get("queryType"))

print(GPTFive)
print(GPTFiveQuery)