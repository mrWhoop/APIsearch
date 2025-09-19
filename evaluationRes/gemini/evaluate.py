import pymongo
from pymongo import MongoClient
from pymongo.errors import OperationFailure
from pathlib import Path
import json

client = MongoClient("mongodb://localhost:27017/")
db = client["api"]
collection = db["apis"]

complex = Path("complex")
malicious = Path("malicious")
named = Path("named")
simple = Path("simple")

# -------------------
# complex
# -------------------

print('COMPLEX')
for file in complex.iterdir():
    if file.is_file():
        print(f"--- {file.name} ---")
        try:
            data = json.loads(file.read_text(encoding="utf-8"))
            queries = data["responses"]
            for query in queries:
                mongoQuery = json.loads(query[7:-3].strip())['query']
                apis = collection.find(mongoQuery)
                print(collection.count_documents(mongoQuery))


        except json.JSONDecodeError as e:
            print(f"Error decoding {file.name}: {e}")

print('NAMED')
for file in named.iterdir():
    if file.is_file():
        print(f"--- {file.name} ---")
        try:
            data = json.loads(file.read_text(encoding="utf-8"))
            queries = data["responses"]
            for query in queries:
                mongoQuery = json.loads(query[7:-3].strip())['query']
                try:
                    apis = collection.find(mongoQuery)
                    print(collection.count_documents(mongoQuery))
                except pymongo.errors.OperationFailure as e:
                    print(f"error: {e}")
                    print(mongoQuery)


        except json.JSONDecodeError as e:
            print(f"Error decoding {file.name}: {e}")

print('SIMPLE')
for file in simple.iterdir():
    if file.is_file():
        print(f"--- {file.name} ---")
        try:
            data = json.loads(file.read_text(encoding="utf-8"))
            queries = data["responses"]
            for query in queries:
                mongoQuery = json.loads(query[7:-3].strip())['query']
                try:
                    apis = collection.find(mongoQuery)
                    print(collection.count_documents(mongoQuery))
                except pymongo.errors.OperationFailure as e:
                    print(f"error: {e}")
                    print(mongoQuery)


        except json.JSONDecodeError as e:
            print(f"Error decoding {file.name}: {e}")

print('MALICIOUS')
for file in malicious.iterdir():
    if file.is_file():
        print(f"--- {file.name} ---")
        try:
            data = json.loads(file.read_text(encoding="utf-8"))
            queries = data["responses"]
            for query in queries:
                mongoQuery = json.loads(query[7:-3].strip())['query']
                apis = collection.find(mongoQuery)
                print(collection.count_documents(mongoQuery))


        except json.JSONDecodeError as e:
            print(f"Error decoding {file.name}: {e}")
