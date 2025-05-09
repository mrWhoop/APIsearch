import chromadb
from openai import OpenAI
import os
from app.extensions import mongo

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
OpenAI_client = OpenAI(api_key=OPENAI_API_KEY)

def createCollection():

    chroma_client = chromadb.PersistentClient(path="dataRAG/chroma")
    chroma_collection = chroma_client.create_collection(name="gptAPI")
    apis = mongo.db.apis.find()

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

        embedding = response.data[0].embedding

        chroma_collection.add(documents=[document], embeddings=[embedding], ids=[chroma_id], metadatas=[metadata])

    return
