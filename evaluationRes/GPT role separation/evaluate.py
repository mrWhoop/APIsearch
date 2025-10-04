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
complexTextError = 0
allComplex = 0
complexInvalidJSON = 0
for file in complex.iterdir():
    if file.is_file():
        print()
        print(f"--- {file.name} ---")
        try:
            data = json.loads(file.read_text(encoding="utf-8"))
            queries = data["responses"]
            for query in queries:
                allComplex += 1
                try:
                    mongoQuery = json.loads(query)
                except json.JSONDecodeError as e:
                    complexInvalidJSON += 1
                try:
                    apis = collection.find(mongoQuery)
                    print(collection.count_documents(mongoQuery))
                except pymongo.errors.OperationFailure as e:
                    print(f"error: {e}")
                    print(mongoQuery)
                    complexTextError += 1


        except json.JSONDecodeError as e:
            print(f"Error decoding: {file.name}: {e}")


print('******************************************************')
print('NAMED')
namedTextError = 0
allNamed = 0
namedInvalidJSON = 0
for file in named.iterdir():
    if file.is_file():
        print()
        print(f"--- {file.name} ---")
        try:
            data = json.loads(file.read_text(encoding="utf-8"))
            queries = data["responses"]
            for query in queries:
                allNamed += 1
                try:
                    mongoQuery = json.loads(query)
                except json.JSONDecodeError as e:
                    namedInvalidJSON += 1
                try:
                    apis = collection.find(mongoQuery)
                    print(collection.count_documents(mongoQuery))
                except pymongo.errors.OperationFailure as e:
                    print(f"error: {e}")
                    print(mongoQuery)
                    namedTextError += 1


        except json.JSONDecodeError as e:
            print(f"Error decoding {file.name}: {e}")

print('******************************************************')
print('SIMPLE')
simpleTextError = 0
allSimple = 0
simpleInvalidJSON = 0
for file in simple.iterdir():
    if file.is_file():
        print()
        print(f"--- {file.name} ---")
        try:
            data = json.loads(file.read_text(encoding="utf-8"))
            queries = data["responses"]
            for query in queries:
                allSimple += 1
                try:
                    mongoQuery = json.loads(query)
                except json.JSONDecodeError as e:
                    simpleInvalidJSON += 1
                try:
                    apis = collection.find(mongoQuery)
                    print(collection.count_documents(mongoQuery))
                except pymongo.errors.OperationFailure as e:
                    print(f"error: {e}")
                    print(mongoQuery)
                    simpleTextError += 1


        except json.JSONDecodeError as e:
            print(f"Error decoding {file.name}: {e}")


print('******************************************************')
print('MALICIOUS')
maliciousTextError = 0
allMalicious = 0
maliciousInvalidJSON = 0
for file in malicious.iterdir():
    if file.is_file():
        print()
        print(f"--- {file.name} ---")
        try:
            data = json.loads(file.read_text(encoding="utf-8"))
            queries = data["responses"]
            for query in queries:
                allMalicious += 1
                try:
                    mongoQuery = json.loads(query)
                except json.JSONDecodeError as e:
                    maliciousInvalidJSON += 1
                try:
                    apis = collection.find(mongoQuery)
                    print(collection.count_documents(mongoQuery))
                except pymongo.errors.OperationFailure as e:
                    print(f"error: {e}")
                    print(mongoQuery)
                    maliciousTextError += 1


        except json.JSONDecodeError as e:
            print(f"Error decoding {file.name}: {e}")

print('*****************************************')
print('SIMPLE', allSimple, simpleTextError, 1 - (simpleTextError/allSimple), 'Invalid JSON: ', simpleInvalidJSON)
print('NAMED', allNamed, namedTextError, 1 - (namedTextError/allNamed), 'Invalid JSON: ', namedInvalidJSON)
print('COMPLEX', allComplex, complexTextError, 1 - (complexTextError/allComplex), 'Invalid JSON: ', complexInvalidJSON)
print('MALICIOUS', allMalicious, maliciousTextError, 1 - (maliciousTextError/allMalicious), 'Invalid JSON: ', maliciousInvalidJSON)

