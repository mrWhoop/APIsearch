from json import JSONDecodeError

import meilisearch
from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from mpmath.calculus.extrapolation import limit
from numpy.random import default_rng
from pymongo.errors import OperationFailure

from ..extensions import mongo
from support_scripts.populate_database import populate_database
from support_scripts.populate_search_index import populate_search_index, documents
from support_scripts.create_chroma_chatGPT_embeddings import createCollection as GPT
from support_scripts.create_chroma_Gemini_embeddings import createCollection as GEMINI
from support_scripts.create_chroma_chatGPT_embeddings import createCollectionMeta as GPTmeta
from support_scripts.create_chroma_Gemini_embeddings import createCollectionMeta as GEMINImeta
from support_scripts.create_chroma_chatGPT_embeddings import createCollectionDescriptive as GPTdescriptive
from support_scripts.create_chroma_Gemini_embeddings import createCollectionDescriptive as GEMINIdescriptive
from support_scripts.countTokens import countGPTtokens
from app.models.api import Api, EndPoint
import os
from openai import OpenAI
import chromadb
from chromadb.config import Settings
import google.generativeai as genai
from dotenv import load_dotenv
import json
import time

from support_scripts import evaluation

load_dotenv()

MEILISEARCH_SECRET = os.environ['MEILISEARCH_SECRET']
MEILISEARCH_INDEX = os.environ['MEILISEARCH_INDEX']

searchClient = meilisearch.Client('http://127.0.0.1:7700', MEILISEARCH_SECRET)
searchIndex = searchClient.index(MEILISEARCH_INDEX)


main_blueprint = Blueprint('main', __name__)

def compareGPT(docs):
    OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
    OpenAI_client = OpenAI(api_key=OPENAI_API_KEY)

    document = docs['documents'][0]
    metadata = docs['metadatas'][0]

    documentsString = "You are given five documents:\n\n---\n"
    for i in range(len(document)):
        documentsString = documentsString + "[" + metadata[i]['name'] + "]\n" + document[i] + "\n---\n\n"

    documentsString = documentsString + "Task: Compare these documents. Provide 3 sections in HTML: 1) similarities, 2) differences, 3) unique points per document. Keep each section concise. Return only HTML."

    print("executing GPT prompt")
    start = time.time()
    GPTresponse = OpenAI_client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert document analyst. Compare the provided documents and produce a concise comparative analysis. Do NOT include <script> tags or inline event handlers. Use semantic HTML (sections, headings, lists). Keep style minimal — no external CSS links."},
            {"role": "user", "content": documentsString}
        ],
        temperature=0.2
    )
    end = time.time()

    return GPTresponse.choices[0].message.content.strip() + "<section>" + "Time to execute: " + str(end-start) + " sec</section>"

def compareGemini(docs):
    genai.configure(api_key=os.environ['GEMINI_API_KEY'])
    modelGemini = genai.GenerativeModel('gemini-2.5-pro')

    prompt = """You are an expert document analyst. Your task is to compare provided documents and produce a concise comparative analysis. Do NOT include <script> tags or inline event handlers. Use semantic HTML (sections, headings, lists). Keep style minimal — no external CSS links.
                
                ### INSTRUCTIONS:
                1. **Analyze and Compare:** Review the text from all documents to identify the key **similarities, differences, and unique points** 
                2. **Strict Grounding:** Base your entire response *only* on the content provided in the [DOCUMENT] section. Do not use outside knowledge or make assumptions.
                3. **Output Format:** **Use semantic HTML (sections, headings, lists)** Provide 3 sections in HTML: 1) similarities, 2) differences, 3) unique points per document. Keep each section concise. Return only HTML. Keep style minimal — no external CSS links.
                
                ### CONTEXT:
                
    """

    document = docs['documents'][0]
    metadata = docs['metadatas'][0]

    documentsString = ""
    for i in range(len(document)):
        documentsString = documentsString + "####[" + metadata[i]['name'] + "]\n" + "[" + document[i] + "]\n\n"

    prompt = prompt + documentsString

    print("executing Gemini prompt")
    start = time.time()
    response = modelGemini.generate_content(prompt)
    end = time.time()
    response = response.candidates[0].content.parts[0].text

    return response + "<section>" + "Time to execute: " + str(end-start) + " sec</section>"

@main_blueprint.route('/support/populate_search_index')
def populate_search_index_call():
    populate_search_index()
    return jsonify({'status': 'Populating meilisearch done.'})

@main_blueprint.route('/support/populate_database')
def populate_database_call():

    if mongo.db.apis.count_documents({}) > 0:
        mongo.db.apis.delete_many({})
        populate_database()
        populate_search_index()
        apis = mongo.db.apis.find()
    else:
        populate_database()
        populate_search_index()
        apis = mongo.db.apis.find()

    return jsonify(apis)

@main_blueprint.route('/support/evaluateGemini')
def evaluateGemini_call():
#    evaluation.repeatabilityTestGemini(evaluation.simpleQuery, "simple", 10, mongo)
#    evaluation.repeatabilityTestGemini(evaluation.namedQuery, "named", 10, mongo)
#    evaluation.repeatabilityTestGemini(evaluation.complexQuery, "complex", 10, mongo)
#    evaluation.repeatabilityTestGemini(evaluation.maliciousQuery, "malicious", 10, mongo)
    return jsonify({'status': 'Gemini repeatability evaluation done.'})

@main_blueprint.route('/support/evaluateGPT')
def evaluateGPT_call():
    # evaluation.repeatabilityTestGPT(evaluation.simpleQuery, "simple", 10, mongo)
    # evaluation.repeatabilityTestGPT(evaluation.namedQuery, "named", 10, mongo)
    # evaluation.repeatabilityTestGPT(evaluation.complexQuery, "complex", 10, mongo)
    # evaluation.repeatabilityTestGPT(evaluation.maliciousQuery, "malicious", 10, mongo)
    # evaluation.repeatabilityTestGPT(evaluation.specificQuerry, "specific", 10, mongo)
    return jsonify({'status': 'GPT role separation repeatability evaluation done.'})

@main_blueprint.route('/support/create_GPT')
def createGPTcollection():
    # GPT role separation()
    # GPTmeta()
    # GPTdescriptive()
    return jsonify({'status': 'ChatGPT done.'})

@main_blueprint.route('/support/create_Gemini')
def createGeminiCollection():
    # GEMINI()
    # GEMINImeta()
    # GEMINIdescriptive()
    return jsonify({'status': 'Gemini done.'})

@main_blueprint.route('/support/count_tokens')
def countTokens():
    tokens = countGPTtokens()
    tokenData = {
        'GPT_embeddings': tokens
    }
    return jsonify(tokenData)

def databaseQuerySearchGemini(userQuery):

    genai.configure(api_key=os.environ['GEMINI_API_KEY'])

    prompt = """
        You are an expert MongoDB query generator. Your sole task is to generate the `query` document that would be passed directly into a `db.collection.find(query)` method in MongoDB.

        **Output Format:**
        * Always return a JSON object.
        * The JSON object MUST have a key `query` whose value is the MongoDB query document.
        * Do NOT include the `db.collection.find()` call itself.
        * Do NOT include any explanatory text, comments, or extra newlines outside the JSON structure.

        ---

        **MongoDB `API` Collection Schema:**

        ```json
        {
          "_id": { "type": "ObjectId" },
          "name": { "type": "string",
                    "description": "API name"
                    },
          "description": { "type": "string",
                            "description": "API description"
                        },
          "api_keywords": { "type": ["string"] },
          "popularity": {"type": "number",
                         "description": "A calculated popularity score for the product, ranging from 0 to 10, where 0 is least popular and 10 is most popular."
                         },
          "service_level": {"type": "number",
                         "description": "A calculated service level score for the product, ranging from 0 to 10, where 0 is least reliable and 10 is most reliable."
                         },
          "latency": {"type": "number",
                         "description": "A latency measure for the product, ranging from 0 to 1000, measured in milliseconds where 0 is most responsive and 1000 is least responsive."
                         },
          "reliability": {"type": "number",
                         "description": "A reliability measure for the product, ranging from 0 to 10, ranging from 0 to 10, where 0 is least reliable and 10 is most reliable."
                         },
          "https": { "type": "boolean",
                    "description": "Field indicating if API is using https or not."},
          "authentication": { "type": "string",
                    "description": "Field indicating API authentication method, possible options are None, apiKey, OAuth"},
          "cors": { "type": "boolean",
                    "description": "Field indicating API if API is using cors or not."},
          "type": { "type": "string",
                    "description": "Field indicating API response type, possible options are REST, GraphQL, XML."},
          "category": { "type": "string",
                    "description": "Field indicating API category, possible options are: Animals, Anime, Anti-Malware, Art and Design, Books, Business, Calendar, Cloud storage and File Sharing, Continuous Integration, Cryptocurrency, Currency Exchange, Data Validation, Dictionaries, Disasters, Documents & Productivity, Education, Enviroment, Events, Finance, Food & Drink, Fraud Prevention, Health, Jobs, Machine Learning, Music, News, Open Data, Open Source Projects, Patent, Personality, Photography, Science & Math, Security, Sports & Fitness, Test Data, Text Analysis, Tracking, URL Shorteners, Vehicle, Weather"},          
        }
        ```
        Request:
    """

    modelGemini = genai.GenerativeModel('gemini-2.5-pro') #, system_instruction=prompt)

    response = modelGemini.generate_content(prompt)
    response = response.candidates[0].content.parts[0].text

    print("GEMINI", response)

    if response.startswith("```json") and response.endswith("```"):
        response = response[7:-3].strip()
    else:
        return None

    try:
        query_response = json.loads(response)["query"]
    except JSONDecodeError:
        print(response)
        return None

    result = mongo.db.apis.find(query_response)

    res = list()

    for document in result:
        # print(f"ID: {document['_id']}, Data: {document}")
        r = {
            "name": document['name'],
            "category": document['category'],
            "description": document['description'],
            "docs": document['docs'],
        }
        res.append(r)

    return res

def databaseQuerySearchGPT(userQuery):

    OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
    OpenAI_client = OpenAI(api_key=OPENAI_API_KEY)

    prompt = f"""
                 You are a MongoDB expert. Convert this user search input to a MongoDB query.
                 The MongoDB collection has these fields:
                 - name (string)
                 - description (string)
                 - api_keywords (list of strings, to search here use $elemMatch)
                 - popularity (0-10, number interval, 0 indicating least popular and 10 indicating most popular)
                 - service_level (0-10, number interval, 0 indicating lowest service level and 10 indicating highest service level)
                 - latency (0-1000 number interval in miliseconds, 0 indicating most responsive and 1000 indicating least responsive)
                 - reliability (0-10, number interval, 0 indicating least reliable and 10 indicating most reliable)
                 - https (boolean, indicating whether API uses https)
                 - authentication (string, possible options are: None, apiKey, OAuth)
                 - cors (boolean, indicating whether API uses CORS)
                 - type (string, possible options are REST, GraphQL, XML)
                 - category (string, possible options are: Animals, Anime, Anti-Malware, Art and Design, Books, Business, Calendar, Cloud storage and File Sharing, Continious Integration, Cryptocurrency, Currency Exchange, Data Validation, Dictionaries, Disasters, Documents & Productivity, Education, Enviroment, Events, Finance, Food & Drink, Fraud Prevention, Health, Jobs, Machine Learning, Music, News, Open Data, Open Source Projects, Patent, Personality, Photography, Science & Math, Security, Sports & Fitness, Test Data, Text Analysis, Tracking, URL Shorteners, Vehicle, Weather)

                Use regular expressions for approximate matches and ranges for "reliable", "popular", "fast" etc. only if user query calls for it.
                Respond with only a JSON object that can be used in db.collection.find().
              """

# - category (string, possible options are: Animals, Anime, Anti-Malware, Art and Design, Books, Business, Calendar, Cloud storage and File Sharing, Continious Integration, Cryptocurrency, Currency Exchange, Data Validation, Dictionaries, Disasters, Documents & Productivity, Education, Enviroment, Events, Finance, Food & Drink, Fraud Prevention, Health, Jobs, Machine Learning, Music, News, Open Data, Open Source Projects, Patent, Personality, Photography, Science & Math, Security, Sports & Fitness, Test Data, Text Analysis, Tracking, URL Shorteners, Vehicle, Weather)

    GPTresponse = OpenAI_client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": userQuery}
        ],
        temperature=0.2
    )

    print("GPT role separation call:", GPTresponse.choices[0].message.content.strip())

    try:
        mongoQuery = json.loads(GPTresponse.choices[0].message.content.strip())
        result = mongo.db.apis.find(mongoQuery)

        res = list()

        for document in result:
            # print(f"ID: {document['_id']}, Data: {document}")
            r = {
                "name": document['name'],
                "category": document['category'],
                "description": document['description'],
                "docs": document['docs'],
                "type": document['type'],
                "https": document['https'],
                "popularity": document['popularity'],
                "latency": document['latency'],
                "reliability": document['reliability'],
                "service_level": document['service_level'],
                "cors": document['cors'],
                "authentication": document['authentication'],
            }
            res.append(r)

        return res

    except JSONDecodeError:
        print("JSONerror:", GPTresponse.choices[0].message.content.strip())
        return []

    except OperationFailure as e:
        print(e)
        GPTresponse = OpenAI_client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": userQuery}
            ],
            temperature=0.2
        )
        print("GPT role separation call retry:", GPTresponse.choices[0].message.content.strip())

        try:
            mongoQuery = json.loads(GPTresponse.choices[0].message.content.strip())
            result = mongo.db.apis.find(mongoQuery)

            res = list()

            for document in result:
                r = {
                    "name": document['name'],
                    "category": document['category'],
                    "description": document['description'],
                    "docs": document['docs'],
                    "type": document['type'],
                    "https": document['https'],
                    "popularity": document['popularity'],
                    "latency": document['latency'],
                    "reliability": document['reliability'],
                    "service_level": document['service_level'],
                    "cors": document['cors'],
                    "authentication": document['authentication'],
                }
                res.append(r)
        except OperationFailure as e:
            print("Retry failed.", e)
            return []

        return res


@main_blueprint.route('/search')
@cross_origin()
def search():

    OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
    OpenAI_client = OpenAI(api_key=OPENAI_API_KEY)

    genai.configure(api_key=os.environ['GEMINI_API_KEY'])
    embedding_model_name = 'models/gemini-embedding-exp-03-07'

    chroma_client = chromadb.PersistentClient(path="dataRAG/chroma")

    chroma_GPT_collection = chroma_client.get_collection(name="gptAPI")
    chroma_Gemini_collection = chroma_client.get_collection(name="GeminiAPI")

    chroma_GPT_collection_meta = chroma_client.get_collection(name="gptAPImeta")
    chroma_Gemini_collection_meta = chroma_client.get_collection(name="GeminiAPImeta")

    chroma_GPT_collection_desc = chroma_client.get_collection(name="gptAPIdescriptive")
    chroma_Gemini_collection_desc = chroma_client.get_collection(name="GeminiAPIdescriptive")

    query = request.args.get('q')
    ai = request.args.get('ai')

    if ai == 'GPT':
        query_GPT_embedding = OpenAI_client.embeddings.create(model="text-embedding-ada-002", input=query).data[0].embedding
        resultsGPT = chroma_GPT_collection.query(query_embeddings=[query_GPT_embedding], n_results=5)
        print(resultsGPT['documents'])
        return jsonify({"results": resultsGPT["metadatas"][0]})

    elif ai == 'GPTmeta':
        query_GPT_embedding = OpenAI_client.embeddings.create(model="text-embedding-ada-002", input=query).data[0].embedding
        resultsGPTmeta = chroma_GPT_collection_meta.query(query_embeddings=[query_GPT_embedding], n_results=5)
        print(resultsGPTmeta['documents'])
        return jsonify({"results": resultsGPTmeta["metadatas"][0]})

    elif ai == 'Gemini':
        query_Gemini_embedding = genai.embed_content(model=embedding_model_name, content=query)['embedding']
        resultsGemini = chroma_Gemini_collection.query(query_embeddings=[query_Gemini_embedding], n_results=5)
        print(resultsGemini['documents'])
        return jsonify({"results": resultsGemini["metadatas"][0]})

    elif ai == 'Geminimeta':
        query_Gemini_embedding = genai.embed_content(model=embedding_model_name, content=query)['embedding']
        resultsGeminiMeta = chroma_Gemini_collection_meta.query(query_embeddings=[query_Gemini_embedding], n_results=5)
        print(resultsGeminiMeta['documents'])
        return jsonify({"results": resultsGeminiMeta["metadatas"][0]})

    elif ai == 'MeiliSearch':

        search_results = searchIndex.search(query, {"limit": 5})['hits']

        result = list()

        for sr in search_results:
            res = {
                "name": sr['name'],
                "category": sr['category'],
                "description": sr['description'],
                "docs": sr['docs'],
            }

            result.append(res)

        return jsonify({"results": result})

    elif ai == 'GPTprompt':
        data = databaseQuerySearchGPT(query)
        return jsonify({"results": data})

    elif ai == 'GPTdesc':
        query_GPT_embedding = OpenAI_client.embeddings.create(model="text-embedding-ada-002", input=query).data[0].embedding
        resultsGPTdesc = chroma_GPT_collection_desc.query(query_embeddings=[query_GPT_embedding], n_results=5)
        print(resultsGPTdesc['documents'])
        return jsonify({"results": resultsGPTdesc["metadatas"][0]})

    elif ai == 'Geminidesc':
        query_Gemini_embedding = genai.embed_content(model=embedding_model_name, content=query)['embedding']
        resultsGeminiDesc = chroma_Gemini_collection_desc.query(query_embeddings=[query_Gemini_embedding], n_results=5)
        print(resultsGeminiDesc['documents'])
        return jsonify({"results": resultsGeminiDesc["metadatas"][0]})
    else:
        query_Gemini_embedding = genai.embed_content(model=embedding_model_name, content=query)['embedding']
        resultsGeminiDesc = chroma_Gemini_collection_desc.query(query_embeddings=[query_Gemini_embedding], n_results=5)

        return jsonify({"results": resultsGeminiDesc["metadatas"][0],
                        "GPTsummary": compareGPT(resultsGeminiDesc),
                        "GeminiSummary": compareGemini(resultsGeminiDesc)
                        })
