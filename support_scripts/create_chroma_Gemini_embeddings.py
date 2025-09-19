import chromadb
import os
from app.extensions import mongo
import google.generativeai as genai
import time

genai.configure(api_key=os.environ['GEMINI_API_KEY'])
embedding_model_name='models/gemini-embedding-exp-03-07'

def createCollection():

    chroma_client = chromadb.PersistentClient(path="dataRAG/chroma")
    chroma_client.delete_collection("GeminiAPI")
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
            'popularity': str(api['popularity']),
            'service_level': str(api['service_level']),
            'latency': str(api['latency']),
            'reliability': str(api['reliability']),
            'authentication': str(api['authentication']),
            'https': str(api['https']),
            'cors': str(api['cors'])
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
    chroma_client.delete_collection("GeminiAPImeta")
    chroma_collection = chroma_client.create_collection(name="GeminiAPImeta")
    apis = mongo.db.apis.find()

    for api in apis:
        document = "Name: " + api['name'] + "\n" + "Description: " + api['description'] + "\n" + "Popularity: " + str(api['popularity']) + "/10 \n" + "Service level: " + str(api['service_level']) + "/10\n" + "Latency: " + str(api['latency']) + "\n" + "Reliability: " + str(api['reliability']) + "/10\n" + "Category: " + api['category'] + "\n"
        chroma_id = str(api['_id'])

        metadata = {
            'name': str(api['name']),
            'description': str(api['description']),
            'docs': str(api['docs']),
            'category': str(api['category']),
            'popularity': str(api['popularity']),
            'service_level': str(api['service_level']),
            'latency': str(api['latency']),
            'reliability': str(api['reliability']),
            'authentication': str(api['authentication']),
            'https': str(api['https']),
            'cors': str(api['cors'])
        }

        # here we get gemini embeddings

        embedding = genai.embed_content(
            model=embedding_model_name,
            content=document)

        embedding = embedding['embedding']

        time.sleep(5)

        chroma_collection.add(documents=[document], embeddings=[embedding], ids=[chroma_id], metadatas=[metadata])

    return

def createCollectionGeminiDescriptive():

    chroma_client = chromadb.PersistentClient(path="dataRAG/chroma")
    chroma_client.delete_collection("GeminiAPImeta")
    chroma_collection = chroma_client.create_collection(name="GeminiAPIdescriptive")
    apis = mongo.db.apis.find()

    for api in apis:

        popularity = api['popularity'] # very unpopular, unpopular, popular, very popular
        service_level = api['service_level'] # very bad service level, bad service level, good service level, very good service level
        latency = api['latency'] # very unresponsive, unresponsive, responsive, very responsive
        reliability = api['reliability'] # very unreliable, unreliable, reliable, very reliable
        authentication = api['authentication'] # pul out of db, if null skip
        https = api['https'] # True --> uses https; False --> uses http; null --> skip
        cors = api['cors'] # True --> uses cors; False --> does not use cors; null skip
        category = api['category'] # Falls into category
        type = api['type'] # Is 'type' API

        document = "Name: " + api['name'] + "\n" + "Description: " + api['description'] + "\n" + "Popularity: " + str(api['popularity']) + "/10 \n" + "Service level: " + str(api['service_level']) + "/10\n" + "Latency: " + str(api['latency']) + "\n" + "Reliability: " + str(api['reliability']) + "/10\n" + "Category: " + api['category'] + "\n"
        chroma_id = str(api['_id'])

        metadata = {
            'name': str(api['name']),
            'description': str(api['description']),
            'docs': str(api['docs']),
            'category': str(api['category']),
            'popularity': str(api['popularity']),
            'service_level': str(api['service_level']),
            'latency': str(api['latency']),
            'reliability': str(api['reliability']),
            'authentication': str(api['authentication']),
            'https': str(api['https']),
            'cors': str(api['cors'])
        }

        # here we get gemini embeddings

        embedding = genai.embed_content(
            model=embedding_model_name,
            content=document)

        embedding = embedding['embedding']

        time.sleep(5)

        chroma_collection.add(documents=[document], embeddings=[embedding], ids=[chroma_id], metadatas=[metadata])

    return
