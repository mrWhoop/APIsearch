import pymongo
from pymongo import MongoClient
from pymongo.errors import OperationFailure
from pathlib import Path
import json
import chromadb
import meilisearch

import os
from dotenv import load_dotenv

load_dotenv()

MEILISEARCH_SECRET = os.environ['MEILISEARCH_SECRET']
MEILISEARCH_INDEX = os.environ['MEILISEARCH_INDEX']
MEILISEARCH_INDEX_EMM = os.environ['MEILISEARCH_INDEX_EMM']

searchClient = meilisearch.Client('http://127.0.0.1:7700', MEILISEARCH_SECRET)
searchIndex = searchClient.index(MEILISEARCH_INDEX)
searchIndexEmm = searchClient.index(MEILISEARCH_INDEX_EMM)

def print_meilisearch_configuration(index):
    settings = index.get_settings()

    config = {
        "searchableAttributes":
            settings.get("searchableAttributes"),

        "rankingRules":
            settings.get("rankingRules"),

        "embedders":
            settings.get("embedders")
    }

    print(json.dumps(
        config,
        indent=4,
        ensure_ascii=False
    ))

print_meilisearch_configuration(searchIndex)
print_meilisearch_configuration(searchIndexEmm)


client = MongoClient(os.environ['MONGO_READWRITE_URI'])
db = client["api"]
collection = db["apis"]

apis = collection.find()

categories = set()
types = set()
authentication = set()

for api in apis:
    categories.add(api.get('category'))
    types.add(api.get('type'))
    authentication.add(api.get('authentication'))

print()
print(types, len(types))
print(categories, len(categories))
print(authentication, len(authentication))

# check croma
chroma_client = chromadb.PersistentClient(path="../dataRAG/chroma")

chroma_GPT_collection = chroma_client.get_collection(name="gptAPI")
chroma_Gemini_collection = chroma_client.get_collection(name="GeminiAPI")

chroma_GPT_collection_meta = chroma_client.get_collection(name="gptAPImeta")
chroma_Gemini_collection_meta = chroma_client.get_collection(name="GeminiAPImeta")

chroma_GPT_collection_desc = chroma_client.get_collection(name="gptAPIdescriptive")
chroma_Gemini_collection_desc = chroma_client.get_collection(name="GeminiAPIdescriptive")

print(chroma_GPT_collection.count())
print(chroma_Gemini_collection.count())
print(chroma_GPT_collection_meta.count())
print(chroma_Gemini_collection_meta.count())
print(chroma_GPT_collection_desc.count())
print(chroma_Gemini_collection_desc.count())

print(chroma_GPT_collection.metadata)
print(chroma_Gemini_collection.metadata)
print(chroma_GPT_collection_meta.metadata)
print(chroma_Gemini_collection_meta.metadata)
print(chroma_GPT_collection_desc.metadata)
print(chroma_Gemini_collection_desc.metadata)

import chromadb
import json

client = chromadb.PersistentClient(path="../dataRAG/chroma")
print(chromadb.__version__)

for collection in client.list_collections():
    print(f"\nCollection: {collection.name}")
    print("Metadata:")
    print(json.dumps(collection.metadata, indent=2, default=str))
    print(collection.metadata)
    print("Configuration:")
    print(json.dumps(collection.configuration, indent=2, default=str))

    # Embedding dimension
    sample = collection.get(
        limit=1,
        include=["embeddings"]
    )

    embeddings = sample["embeddings"]

    if embeddings is not None and len(embeddings) > 0:
        dimension = len(embeddings[0])
        print(f"Embedding dimension: {dimension}")
    else:
        print("Embedding dimension: unavailable (empty collection)")


