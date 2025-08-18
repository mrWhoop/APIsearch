from json import JSONDecodeError

import meilisearch
from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from mpmath.calculus.extrapolation import limit
from pymongo.errors import OperationFailure

from ..extensions import mongo
from support_scripts.populate_database import populate_database
from support_scripts.populate_search_index import populate_search_index
from support_scripts.create_chroma_chatGPT_embeddings import createCollection as GPT
from support_scripts.create_chroma_Gemini_embeddings import createCollection as GEMINI
from support_scripts.create_chroma_chatGPT_embeddings import createCollectionMeta as GPTmeta
from support_scripts.create_chroma_Gemini_embeddings import createCollectionMeta as GEMINImeta
from support_scripts.countTokens import countGPTtokens
from app.models.api import Api, EndPoint
import os
from openai import OpenAI
import chromadb
from chromadb.config import Settings
import google.generativeai as genai
from dotenv import load_dotenv
import json

load_dotenv()

MEILISEARCH_SECRET = os.environ['MEILISEARCH_SECRET']
MEILISEARCH_INDEX = os.environ['MEILISEARCH_INDEX']

searchClient = meilisearch.Client('http://127.0.0.1:7700', MEILISEARCH_SECRET)
searchIndex = searchClient.index(MEILISEARCH_INDEX)


main_blueprint = Blueprint('main', __name__)

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

@main_blueprint.route('/support/create_GPT')
def createGPTcollection():
    GPT()
    GPTmeta()
    return jsonify({'status': 'ChatGPT done.'})

@main_blueprint.route('/support/create_Gemini')
def createGeminiCollection():
    GEMINI()
    GEMINImeta()
    return jsonify({'status': 'Gemini done.'})

@main_blueprint.route('/support/count_tokens')
def countTokens():
    tokens = countGPTtokens()
    tokenData = {
        'GPT_embeddings': tokens
    }
    return jsonify(tokenData)

def databaseQuerySearchGemini(userQuery):
    # Choose a Gemini model. 'gemini-pro' is a good general-purpose model.
    # You might also consider 'gemini-1.5-flash' or 'gemini-1.5-pro' for specific needs.

    genai.configure(api_key=os.environ['GEMINI_API_KEY'])
    modelGemini = genai.GenerativeModel('gemini-1.5-pro')

    prompt = """
        You are an expert MongoDB query generator. Your sole task is to generate the `query` document (and optionally the `projection` document) that would be passed directly into a `db.collection.find(query, projection)` method in MongoDB.

        **Output Format:**
        * Always return a JSON object.
        * The JSON object MUST have a key `query` whose value is the MongoDB query document.
        * If a projection is requested, the JSON object MUST also have a key `projection` whose value is the MongoDB projection document. If no projection is needed, omit the `projection` key.
        * Do NOT include the `db.collection.find()` call itself.
        * Do NOT include any explanatory text, comments, or extra newlines outside the JSON structure.
        * For dates, use the format `{"$date": "YYYY-MM-DDTHH:MM:SSZ"}` to represent `ISODate()`. This is a common way to represent dates for JSON parsing.
        
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
          "category": { "type": "string",
                    "description": "Field indicating API category, possible options are: Animals, Anime, Anti-Malware, Art and Design, Books, Business, Calendar, Cloud storage and File Sharing, Continuous Integration, Cryptocurrency, Currency Exchange, Data Validation, Dictionaries, Disasters, Documents & Productivity, Education, Enviroment, Events, Finance, Food & Drink, Fraud Prevention, Health, Jobs, Machine Learning, Music, News, Open Data, Open Source Projects, Patent, Personality, Photography, Science & Math, Security, Sports & Fitness, Test Data, Text Analysis, Tracking, URL Shorteners, Vehicle, Weather"},          
        }
        ```
        Request: 
    """ + userQuery

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
                 - popularity (0-10, number)
                 - service_level (0-10, number)
                 - latency (0-1000 number in miliseconds)
                 - reliability (0-10, number)
                 - https (boolean, indicating whether API uses https)
                 - authentication (string, possible options are: None, apiKey, OAuth)
                 - cors (boolean, indicating whether API uses CORS)
                 - type (string, possible options are REST, GraphQL, XML)
                
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

    print("GPT", GPTresponse.choices[0].message.content.strip())

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
            }
            res.append(r)

        return res

    except JSONDecodeError:
        print(GPTresponse.choices[0].message.content.strip())
        mongoQuery = None

    except OperationFailure as e:
        print(e)
        return None



@main_blueprint.route('/search')
@cross_origin()
def search():

    # result = {
    #     "results": [{
    #       "name": 'string1',
    #       "category": 'string',
    #       "description": 'string',
    #       "docs": 'string',
    #     },
    #     {
    #         "name": 'string2',
    #         "category": 'string',
    #         "description": 'string',
    #         "docs": 'string',
    #     },
    #     {
    #         "name": 'string3',
    #         "category": 'string',
    #         "description": 'string',
    #         "docs": 'string',
    #     }]
    # }

    OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
    OpenAI_client = OpenAI(api_key=OPENAI_API_KEY)

    genai.configure(api_key=os.environ['GEMINI_API_KEY'])
    embedding_model_name = 'models/gemini-embedding-exp-03-07'

    chroma_client = chromadb.PersistentClient(path="dataRAG/chroma")

    chroma_GPT_collection = chroma_client.get_collection(name="gptAPI")
    chroma_Gemini_collection = chroma_client.get_collection(name="GeminiAPI")

    chroma_GPT_collection_meta = chroma_client.get_collection(name="gptAPImeta")
    chroma_Gemini_collection_meta = chroma_client.get_collection(name="GeminiAPImeta")

    query = request.args.get('q')
    ai = request.args.get('ai')

    ## RAG

    if ai == 'GPT':
        query_GPT_embedding = OpenAI_client.embeddings.create(model="text-embedding-ada-002", input=query).data[0].embedding
        resultsGPT = chroma_GPT_collection.query(query_embeddings=[query_GPT_embedding], n_results=5)
        return jsonify({"results": resultsGPT["metadatas"][0]})

    elif ai == 'GPTmeta':
        query_GPT_embedding = OpenAI_client.embeddings.create(model="text-embedding-ada-002", input=query).data[0].embedding
        resultsGPTmeta = chroma_GPT_collection_meta.query(query_embeddings=[query_GPT_embedding], n_results=5)
        return jsonify({"results": resultsGPTmeta["metadatas"][0]})

    elif ai == 'Gemini':
        query_Gemini_embedding = genai.embed_content(model=embedding_model_name, content=query)['embedding']
        resultsGemini = chroma_Gemini_collection.query(query_embeddings=[query_Gemini_embedding], n_results=5)
        return jsonify({"results": resultsGemini["metadatas"][0]})

    elif ai == 'Geminimeta':
        query_Gemini_embedding = genai.embed_content(model=embedding_model_name, content=query)['embedding']
        resultsGeminiMeta = chroma_Gemini_collection_meta.query(query_embeddings=[query_Gemini_embedding], n_results=5)
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

    elif ai == 'Geminiprompt':
        data = databaseQuerySearchGemini(query)
        return jsonify({"results": data})

    elif ai == 'GPTHybrid':
        # hybrid solution with chroma for GPT
        return

    elif ai == 'GeminiHybrid':
        # hybrid solution with chroma for Gemini
        return
    else:
        # this will be normal search, final best product
        query_Gemini_embedding = genai.embed_content(model=embedding_model_name, content=query)['embedding']
        resultsGeminiMeta = chroma_Gemini_collection_meta.query(query_embeddings=[query_Gemini_embedding], n_results=5)
        return jsonify({"results": resultsGeminiMeta["metadatas"][0]})
