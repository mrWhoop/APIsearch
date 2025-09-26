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

def createCollectionDescriptive():

    chroma_client = chromadb.PersistentClient(path="dataRAG/chroma")
    # chroma_client.delete_collection("GeminiAPIdescriptive")
    chroma_collection = chroma_client.create_collection(name="GeminiAPIdescriptive")

    apis = mongo.db.apis.find()

    for api in apis:

        popularity = api['popularity'] # very unpopular, unpopular, popular, very popular
        service_level = api['service_level'] # very bad service level, bad service level, good service level, very good service level
        latency = api['latency'] # very unresponsive, unresponsive, responsive, very responsive
        reliability = api['reliability'] # very unreliable, unreliable, reliable, very reliable
        authentication = api['authentication'] # pull out of db, if null skip
        https = api['https'] # True --> uses https; False --> uses http; null --> skip
        cors = api['cors'] # True --> uses cors; False --> does not use cors; null skip
        category = str(api['category']) # Falls into category
        type = api['type'] # Is 'type' API

        document = api['name'] + " is " + type + " API.\nIt belongs to " +'"' + category + '"' + " category.\n"

        if authentication is None:
            pass
        else:
            document = document + "It uses " + authentication + " method of authentication.\n"

        if https is None:
            pass
        elif https:
            document = document + "It supports HTTPS.\n"
        else:
            document = document + "It does not support HTTPS.\n"

        if cors is None:
            pass
        elif cors:
            document = document + "It supports CORS.\n"
        else:
            document = document + "It does not support CORS.\n"

        if 0 <= popularity <= 2.5:
            document = document + "It is very unpopular.\n"
        elif 2.5 < popularity <= 5:
            document = document + "It is unpopular.\n"
        elif 5 < popularity <= 7.5:
            document = document + "It is popular.\n"
        elif 7.5 < popularity <= 10:
            document = document + "It is very popular.\n"
        else:
            print("Invalid popularity score.")

        if 0 <= service_level <= 2.5:
            document = document + "It has a very bad service level.\n"
        elif 2.5 < service_level <= 5:
            document = document + "It has a bad service level.\n"
        elif 5 < service_level <= 7.5:
            document = document + "It has a good service level.\n"
        elif 7.5 < service_level <= 10:
            document = document + "It has a very good service level.\n"
        else:
            print("Invalid service level score.")

        if 0 <= latency <= 250:
            document = document + "The API is very unresponsive.\n"
        elif 250 < latency <= 500:
            document = document + "The API is unresponsive.\n"
        elif 500 < latency <= 750:
            document = document + "The API is responsive.\n"
        elif 750 < latency <= 1000:
            document = document + "The API is very responsive.\n"
        else:
            print("Invalid service level score.")

        if 0 <= reliability <= 250:
            document = document + "The API is very unreliable.\n"
        elif 250 < reliability <= 500:
            document = document + "The API is unreliable.\n"
        elif 500 < reliability <= 750:
            document = document + "The API is reliable.\n"
        elif 750 < reliability <= 1000:
            document = document + "The API is very reliable.\n"
        else:
            print("Invalid service level score.")


        document = document + api['description']

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
