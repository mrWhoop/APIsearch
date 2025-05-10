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

def createCollectionMeta():

    chroma_client = chromadb.PersistentClient(path="dataRAG/chroma")
    chroma_collection = chroma_client.get_or_create_collection(name="gptAPImeta")
    apis = mongo.db.apis.find()

    for api in apis:
        document = "Name: " + api['name'] + "\n" + "Description: " + api['description'] + "\n" + "Popularity: " + str(api['popularity']) + "/10 \n" + "Service level: " + str(api['service_level']) + "/10\n" + "Latency: " + str(api['latency']) + "\n" + "Reliability: " + str(api['reliability']) + "/10\n" + "Category: " + api['category'] + '\n'
        chroma_id = str(api['_id'])

        print(document)

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
