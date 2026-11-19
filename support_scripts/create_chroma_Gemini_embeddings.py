import chromadb
import os

from app.extensions import mongo
from google import genai
from google.genai import types
from google.genai.errors import APIError
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

import time

client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])
embedding_model_name='models/gemini-embedding-001'

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(APIError)
)
def embed_single_document(doc_text: str):
    return client.models.embed_content(
        model=embedding_model_name,
        contents=doc_text,
        config=types.EmbedContentConfig(task_type="RETRIEVAL_DOCUMENT")
    )

def createCollection():

    chroma_client = chromadb.PersistentClient(path="dataRAG/chroma")
    chroma_client.delete_collection("GeminiAPI")
    chroma_collection = chroma_client.create_collection(name="GeminiAPI")
    apis = mongo.db.apis.find()

    for api in apis:
        document = api['name'] + "\n" + api['description']
        chroma_id = str(api['_id'])

        metadata = {
            key: value
            for key, value in {
                'id': str(api['_id']),
                'name': api['name'],
                'description': api['description'],
                'docs': api['docs'],
                'category': api['category'],
                'authentication': api['authentication'],
                'https': api['https'],
                'cors': api['cors'],
                'type': api['type']
            }.items()
            if value is not None
        }

        # here we get gemini embeddings

        response = embed_single_document(document)

        embedding = response.embeddings[0].values

        chroma_collection.add(documents=[document], embeddings=[embedding], ids=[chroma_id], metadatas=[metadata])

    return

def createCollectionMeta():

    chroma_client = chromadb.PersistentClient(path="dataRAG/chroma")
    chroma_client.delete_collection("GeminiAPImeta")
    chroma_collection = chroma_client.create_collection(name="GeminiAPImeta")
    apis = mongo.db.apis.find()

    for api in apis:
        document = "Name: " + api['name'] + "\n" + "Type: " + api['type'] + "\n" + "Description: " + api['description'] + "\n" + "Category: " + api['category'] + "\n"

        authentication = api['authentication']
        https = api['https']
        cors = api['cors']

        if authentication is None:
            pass
        else:
            document = document + "Authentication: " + authentication + "\n"

        if https is None:
            pass
        else:
            document = document + "HTTPS: " + str(https) + "\n"

        if cors is None:
            pass
        else:
            document = document + "CORS: " + str(cors) + "\n"

        # random values
        # document = document + "Popularity: " + str(api['popularity']) + "/10 \n" + "Service level: " + str(api['service_level']) + "/10\n" + "Latency: " + str(api['latency']) + " ms\n" + "Reliability: " + str(api['reliability']) + "/10"

        chroma_id = str(api['_id'])

        metadata = {
            key: value
            for key, value in {
                'id': str(api['_id']),
                'name': api['name'],
                'description': api['description'],
                'docs': api['docs'],
                'category': api['category'],
                'authentication': api['authentication'],
                'https': api['https'],
                'cors': api['cors'],
                'type': api['type']
            }.items()
            if value is not None
        }

        # here we get gemini embeddings

        response = embed_single_document(document)

        embedding = response.embeddings[0].values

        chroma_collection.add(documents=[document], embeddings=[embedding], ids=[chroma_id], metadatas=[metadata])

    return

def createCollectionDescriptive():

    chroma_client = chromadb.PersistentClient(path="dataRAG/chroma")
    chroma_client.delete_collection("GeminiAPIdescriptive")
    chroma_collection = chroma_client.create_collection(name="GeminiAPIdescriptive")

    apis = mongo.db.apis.find()

    for api in apis:

        # popularity = api['popularity'] # very unpopular, unpopular, popular, very popular
        # service_level = api['service_level'] # very bad service level, bad service level, good service level, very good service level
        # latency = api['latency'] # very unresponsive, unresponsive, responsive, very responsive
        # reliability = api['reliability'] # very unreliable, unreliable, reliable, very reliable
        authentication = api['authentication'] # pull out of db, if null skip
        https = api['https'] # True --> uses https; False --> uses http; null --> skip
        cors = api['cors'] # True --> uses cors; False --> does not use cors; null skip
        category = str(api['category']) # Falls into category
        type = api['type'] # Is 'type' API

        document = api['name'] + " is " + type + " API.\n"
        document = document + api['description'] + "\n"
        document = document + "It belongs to " + '"' + category + '"' + " category.\n"

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

        # random values
        # if 0 <= popularity <= 2.5:
        #     document = document + "It is very unpopular.\n"
        # elif 2.5 < popularity <= 5:
        #     document = document + "It is unpopular.\n"
        # elif 5 < popularity <= 7.5:
        #     document = document + "It is popular.\n"
        # elif 7.5 < popularity <= 10:
        #     document = document + "It is very popular.\n"
        # else:
        #     print("Invalid popularity score.")
        #
        # if 0 <= service_level <= 2.5:
        #     document = document + "It has a very bad service level.\n"
        # elif 2.5 < service_level <= 5:
        #     document = document + "It has a bad service level.\n"
        # elif 5 < service_level <= 7.5:
        #     document = document + "It has a good service level.\n"
        # elif 7.5 < service_level <= 10:
        #     document = document + "It has a very good service level.\n"
        # else:
        #     print("Invalid service level score.")
        #
        # if 0 <= latency <= 250:
        #     document = document + "The API is very responsive.\n"
        # elif 250 < latency <= 500:
        #     document = document + "The API is responsive.\n"
        # elif 500 < latency <= 750:
        #     document = document + "The API is unresponsive.\n"
        # elif 750 < latency <= 1000:
        #     document = document + "The API is very unresponsive.\n"
        # else:
        #     print("Invalid service level score.")
        #
        # if 0 <= reliability <= 2.5:
        #     document = document + "The API is very unreliable.\n"
        # elif 2.5 < reliability <= 5:
        #     document = document + "The API is unreliable.\n"
        # elif 5 < reliability <= 7.5:
        #     document = document + "The API is reliable.\n"
        # elif 7.5 < reliability <= 10:
        #     document = document + "The API is very reliable.\n"
        # else:
        #     print("Invalid service level score.")

        chroma_id = str(api['_id'])

        metadata = {
            key: value
            for key, value in {
                'id': str(api['_id']),
                'name': api['name'],
                'description': api['description'],
                'docs': api['docs'],
                'category': api['category'],
                'authentication': api['authentication'],
                'https': api['https'],
                'cors': api['cors'],
                'type': api['type']
            }.items()
            if value is not None
        }

        # here we get gemini embeddings

        response = embed_single_document(document)

        embedding = response.embeddings[0].values

        chroma_collection.add(documents=[document], embeddings=[embedding], ids=[chroma_id], metadatas=[metadata])

    return
