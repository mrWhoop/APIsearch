import chromadb
from chromadb.config import Settings
from openai import OpenAI
import os
from app.extensions import mongo

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
OpenAI_client = OpenAI(api_key=OPENAI_API_KEY)

chroma_client = chromadb.PersistentClient(path="/data/chromaGPT")

def createCollection():
    chroma_collection = chroma_client.get_or_create_collection(name="apis")
    apis = mongo.db.apis.find()

    documents = list()
    ids = list()
    metadatas = list()
    embeddings = list()

    for api in apis:
        document = api['name'] + "\n" + api['description']
        chroma_id = str(api['_id'])

        # here you call chatGPT for embedding

        response = OpenAI_client.embeddings.create(
            model="text-embedding-ada-002",
            input=document,
            encoding_format="float"
        )

        metadata = {
            'name': str(api['name']),
            'description': str(api['description']),
            'docs': str(api['docs']),
            'category': str(api['category']),
        }

        embeding = response.data[0].embedding

        documents.append(document)
        ids.append(chroma_id)
        metadatas.append(metadata)
        embeddings.append(embeding)

    chroma_collection.add(documents=documents, ids=ids, metadatas=metadatas)

    return
