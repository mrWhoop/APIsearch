import chromadb
import os
from app.extensions import mongo
import google.generativeai as genai
import time

genai.configure(api_key=os.environ['GEMINI_API_KEY'])
embedding_model_name='models/gemini-embedding-exp-03-07'

def createCollection():

    chroma_client = chromadb.PersistentClient(path="dataRAG/chroma")
    chroma_collection = chroma_client.create_collection(name="GeminiAPI")
    apis = mongo.db.apis.find()

    for api in apis:
        document = api['name'] + "\n" + api['description']
        chroma_id = str(api['_id'])

        metadata = {
            'name': str(api['name']),
            'description': str(api['description']),
            'docs': str(api['docs']),
            'category': str(api['category']),
        }

        # here we get gemini embeddings

        embedding = genai.embed_content(
            model=embedding_model_name,
            content=document)

        embedding = embedding['embedding']

        time.sleep(5)

        chroma_collection.add(documents=[document], embeddings=[embedding], ids=[chroma_id], metadatas=[metadata])

    return

def createCollectionMeta():

    chroma_client = chromadb.PersistentClient(path="dataRAG/chroma")
    chroma_collection = chroma_client.create_collection(name="GeminiAPImeta")
    apis = mongo.db.apis.find()

    for api in apis:
        document = "Name: " + api['name'] + "\n" + "Description: " + api['description'] + "\n" + "Popularity: " + str(api['popularity']) + "/10 \n" + "Service level: " + str(api['service_level']) + "/10\n" + "Latency: " + str(api['latency']) + "\n" + "Reliability: " + str(api['reliability']) + "/10\n" + "Category: " + api['category'] + '\n'
        chroma_id = str(api['_id'])

        metadata = {
            'name': str(api['name']),
            'description': str(api['description']),
            'docs': str(api['docs']),
            'category': str(api['category']),
        }

        # here we get gemini embeddings

        embedding = genai.embed_content(
            model=embedding_model_name,
            content=document)

        embedding = embedding['embedding']

        time.sleep(5)

        chroma_collection.add(documents=[document], embeddings=[embedding], ids=[chroma_id], metadatas=[metadata])

    return
