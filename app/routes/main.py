from json import JSONDecodeError
from unittest import result

import meilisearch
import tiktoken
from flask import Blueprint, jsonify, request, current_app
from flask_cors import cross_origin
from pymongo.errors import OperationFailure
from tenacity import retry_unless_exception_type
from bson import ObjectId

from support_scripts import evaluation
from ..extensions import mongo
from support_scripts.populate_database import populate_database
from support_scripts.populate_search_index import populate_search_index, populate_search_index_embeddings
from support_scripts.evaluationUtility import evaluateExecutionTime, evaluateTokenUsage

from app.utility.promptUtility import generatePrompt, generateComparisonPrompt
from app.utility.validationUtility import validateMongoQuery
import os
from openai import OpenAI
import chromadb

from google import genai
from google.genai import types

from dotenv import load_dotenv
import json
import time

load_dotenv()

MEILISEARCH_SECRET = os.environ['MEILISEARCH_SECRET']
MEILISEARCH_INDEX = os.environ['MEILISEARCH_INDEX']
MEILISEARCH_INDEX_EMM = os.environ['MEILISEARCH_INDEX_EMM']

searchClient = meilisearch.Client('http://127.0.0.1:7700', MEILISEARCH_SECRET)
searchIndex = searchClient.index(MEILISEARCH_INDEX)
searchIndexEmm = searchClient.index(MEILISEARCH_INDEX_EMM)

chroma_client = chromadb.PersistentClient(path="dataRAG/chroma")

chroma_GPT_collection = chroma_client.get_collection(name="gptAPI")
chroma_Gemini_collection = chroma_client.get_collection(name="GeminiAPI")

chroma_GPT_collection_meta = chroma_client.get_collection(name="gptAPImeta")
chroma_Gemini_collection_meta = chroma_client.get_collection(name="GeminiAPImeta")

chroma_GPT_collection_desc = chroma_client.get_collection(name="gptAPIdescriptive")
chroma_Gemini_collection_desc = chroma_client.get_collection(name="GeminiAPIdescriptive")

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
OpenAI_client = OpenAI(api_key=OPENAI_API_KEY)

gemini_client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])

main_blueprint = Blueprint('main', __name__)

def countTokensMeiliSearchHybrid(query):
    encoding = tiktoken.encoding_for_model("text-embedding-3-small")
    return len(encoding.encode(query))

def compareGPT(docs, query, mongoWrite):

    documentsString, prompt = generateComparisonPrompt(docs, query)

    start = time.time()
    GPTresponse = OpenAI_client.chat.completions.create(
        model="gpt-6-luna",
        reasoning_effort="medium",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": documentsString}
        ]
    )
    end = time.time()
    evaluateExecutionTime(model="gpt-6-luna", start=start, end=end, query=query, implementation='GPTComparePrompt', mongo=mongoWrite)
    evaluateTokenUsage(model='gpt-6-luna', inputTokens=GPTresponse.usage.prompt_tokens, thinkingTokens=GPTresponse.usage.completion_tokens_details.reasoning_tokens, outputTokens=GPTresponse.usage.completion_tokens, totalTokens=GPTresponse.usage.total_tokens, query=query, implementation='GPTComparePrompt', mongo=mongoWrite)

    return GPTresponse.choices[0].message.content.strip()

def compareGemini(docs, query, mongoWrite):

    documentsString, prompt = generateComparisonPrompt(docs,query)

    start = time.time()
    response = gemini_client.models.generate_content(
        model='gemini-3.8-flash',
        contents=documentsString,
        config=types.GenerateContentConfig(
            system_instruction=prompt,
            temperature=1.0,
            response_mime_type="text/plain",
            thinking_config=types.ThinkingConfig(
                thinking_level=types.ThinkingLevel.MEDIUM
            ),
            automatic_function_calling=types.AutomaticFunctionCallingConfig(
                disable=True
            )
        )
    )
    end = time.time()
    evaluateExecutionTime(model='gemini-3.8-flash', start=start, end=end, query=query, implementation='GeminiComparePrompt', mongo=mongoWrite)
    evaluateTokenUsage(model='gemini-3.8-flash', inputTokens=response.usage_metadata.prompt_token_count, thinkingTokens=response.usage_metadata.thoughts_token_count, outputTokens=response.usage_metadata.candidates_token_count, totalTokens=response.usage_metadata.total_token_count, query=query, implementation='GeminiComparePrompt', mongo=mongoWrite)

    response = response.text.strip()

    return response

@main_blueprint.route('/support/populate_search_index')
def populate_search_index_call():
    populate_search_index()
    populate_search_index_embeddings()
    return jsonify({'status': 'Populating meilisearch done.'})

@main_blueprint.route('/support/populate_database')
def populate_database_call():

    if mongo.db.apis.count_documents({}) > 0:
        mongo.db.apis.delete_many({})
        populate_database()
        populate_search_index()
        populate_search_index_embeddings()
        apis = mongo.db.apis.find()
    else:
        populate_database()
        populate_search_index()
        apis = mongo.db.apis.find()
        populate_search_index_embeddings()

    return jsonify(apis)

@main_blueprint.route('/support/evaluateGemini')
def evaluateGemini_call():
    mongoWrite = current_app.extensions["mongo_readwrite_client"]

#    evaluation.repeatabilityTestGemini(evaluation.simpleQuery, "simple", 10, mongoWrite)
#    evaluation.repeatabilityTestGemini(evaluation.namedQuery, "named", 10, mongoWrite)
#    evaluation.repeatabilityTestGemini(evaluation.complexQuery, "complex", 10, mongoWrite)
#    evaluation.repeatabilityTestGemini(evaluation.specificQuery, "specific", 10, mongoWrite)

#    evaluation.repeatabilityTestGemini(evaluation.malicious_task_change, "malicious/taskChange", 10, mongoWrite)
#    evaluation.repeatabilityTestGemini(evaluation.malicious_unauthorised_reveal, "malicious/unauthorisedReveal", 10, mongoWrite)
#    evaluation.repeatabilityTestGemini(evaluation.malicious_destructive, "malicious/destructive", 10, mongoWrite)
#    evaluation.repeatabilityTestGemini(evaluation.malicious_cost, "malicious/cost", 10, mongoWrite)

    return jsonify({'status': 'Gemini repeatability evaluation done.'})

@main_blueprint.route('/support/evaluateGPT')
def evaluateGPT_call():
    mongoWrite = current_app.extensions["mongo_readwrite_client"]

#    evaluation.repeatabilityTestGPT(evaluation.simpleQuery, "simple", 10, mongoWrite)
#    evaluation.repeatabilityTestGPT(evaluation.namedQuery, "named", 10, mongoWrite)
#    evaluation.repeatabilityTestGPT(evaluation.complexQuery, "complex", 10, mongoWrite)
#    evaluation.repeatabilityTestGPT(evaluation.specificQuery, "specific", 10, mongoWrite)

#    evaluation.repeatabilityTestGPT(evaluation.malicious_task_change, "malicious/taskChange", 10, mongoWrite)
#    evaluation.repeatabilityTestGPT(evaluation.malicious_unauthorised_reveal, "malicious/unauthorisedReveal", 10, mongoWrite)
#    evaluation.repeatabilityTestGPT(evaluation.malicious_destructive, "malicious/destructive", 10, mongoWrite)
#    evaluation.repeatabilityTestGPT(evaluation.malicious_cost, "malicious/cost", 10, mongoWrite)

    return jsonify({'status': 'GPT repeatability evaluation done.'})

@main_blueprint.route('/support/create_GPT')
def createGPTcollection():
    # GPT()
    # GPTmeta()
    # GPTdescriptive()
    return jsonify({'status': 'OpemAI embeddings done.'})

@main_blueprint.route('/support/create_Gemini')
def createGeminiCollection():
    # GEMINI()
    # GEMINImeta()
    # GEMINIdescriptive()
    return jsonify({'status': 'Gemini done.'})

def databaseQuerySearchGemini(userQuery, mongoWrite):

    system_prompt, user_prompt = generatePrompt(userQuery)

    start = time.time()
    response = gemini_client.models.generate_content(
        model='gemini-3.8-flash',
        contents=user_prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=1.0,
            response_mime_type="application/json",
            thinking_config=types.ThinkingConfig(
                thinking_level=types.ThinkingLevel.MEDIUM
            ),
            automatic_function_calling=types.AutomaticFunctionCallingConfig(
                disable=True
            )
        )
    )
    end = time.time()
    evaluateExecutionTime(model='gemini-3.8-flash', start=start, end=end, query=userQuery, implementation='GeminiPrompt', mongo=mongoWrite)
    evaluateTokenUsage(model='gemini-3.8-flash', inputTokens=response.usage_metadata.prompt_token_count, thinkingTokens=response.usage_metadata.thoughts_token_count, outputTokens=response.usage_metadata.candidates_token_count, totalTokens=response.usage_metadata.total_token_count, query=userQuery, implementation='GeminiPrompt', mongo=mongoWrite)

    response = response.text

    try:
        query_response = json.loads(response)
    except JSONDecodeError:
        print('<GEMINI> Broken JSON:', response)
        return []

    if validateMongoQuery(query_response):
        result = mongo.db.apis.find(query_response).max_time_ms(500).sort({"https": -1, "cors": -1, "authentication": -1}).limit(5)
    else:
        print('<GEMINI> Validator break:', query_response)
        return []

    res = list()

    for document in result:
        r = {
            "id": str(document['_id']),
            "name": document['name'],
            "category": document['category'],
            "description": document['description'],
            "docs": document['docs'],
            "type": document['type'],
            "https": document['https'],
            "cors": document['cors'],
            "authentication": document['authentication'],
        }
        res.append(r)

    return res

def databaseQuerySearchGPT(userQuery, mongoWrite):

    system_prompt, user_prompt = generatePrompt(userQuery)

    start = time.time()
    # ne podpira temperature / privzeto 1.0
    GPTresponse = OpenAI_client.chat.completions.create(
        model="gpt-6-luna",
        reasoning_effort="medium",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    end = time.time()
    evaluateExecutionTime(model='gpt-6-luna', start=start, end=end, query=userQuery, implementation='GPTPrompt', mongo=mongoWrite)
    evaluateTokenUsage(model='gpt-6-luna', inputTokens=GPTresponse.usage.prompt_tokens, thinkingTokens=GPTresponse.usage.completion_tokens_details.reasoning_tokens, outputTokens=GPTresponse.usage.completion_tokens, totalTokens=GPTresponse.usage.total_tokens, query=userQuery, implementation='GPTPrompt', mongo=mongoWrite)

    mongoQuery = GPTresponse.choices[0].message.content

    try:
        mongoQuery = json.loads(mongoQuery)
    except JSONDecodeError:
        print('<GPT> Broken JSON', GPTresponse)
        return []

    if validateMongoQuery(mongoQuery):
        result = mongo.db.apis.find(mongoQuery).max_time_ms(500).sort({"https": -1, "cors": -1, "authentication": -1}).limit(5)
    else:
        print('<GPT> Validator break:', mongoQuery)
        return []

    res = list()

    for document in result:
        r = {
            "id": str(document['_id']),
            "name": document['name'],
            "category": document['category'],
            "description": document['description'],
            "docs": document['docs'],
            "type": document['type'],
            "https": document['https'],
            "cors": document['cors'],
            "authentication": document['authentication'],
        }
        res.append(r)

    return res

@main_blueprint.route('/search')
@cross_origin()
def search():

    query = request.args.get('q')
    ai = request.args.get('ai')
    mongoWrite = current_app.extensions["mongo_readwrite_client"]

    if ai == 'GPT':

        start = time.time()
        OpenAIresponse = OpenAI_client.embeddings.create(model="text-embedding-3-large", input=query)
        end = time.time()
        evaluateExecutionTime(model='text-embedding-3-large', start=start, end=end, query=query, implementation='OpenAIEmbeddingSimple', mongo=mongoWrite)
        evaluateTokenUsage(model=OpenAIresponse.model, inputTokens=OpenAIresponse.usage.prompt_tokens, totalTokens=OpenAIresponse.usage.total_tokens, thinkingTokens=0, outputTokens=0, query=query, implementation='OpenAIEmbeddingSimple', mongo=mongoWrite)

        query_GPT_embedding = OpenAIresponse.data[0].embedding
        resultsGPT = chroma_GPT_collection.query(query_embeddings=[query_GPT_embedding], n_results=5)

        return jsonify({"results": resultsGPT["metadatas"][0]})

    elif ai == 'GPTmeta':

        start = time.time()
        OpenAIresponse = OpenAI_client.embeddings.create(model="text-embedding-3-large", input=query)
        end = time.time()
        evaluateExecutionTime(model='text-embedding-3-large', start=start, end=end, query=query, implementation='OpenAIEmbeddingStructured', mongo=mongoWrite)
        evaluateTokenUsage(model=OpenAIresponse.model, inputTokens=OpenAIresponse.usage.prompt_tokens, totalTokens=OpenAIresponse.usage.total_tokens, thinkingTokens=0, outputTokens=0, query=query, implementation='OpenAIEmbeddingStructured', mongo=mongoWrite)

        query_GPT_embedding = OpenAIresponse.data[0].embedding
        resultsGPTmeta = chroma_GPT_collection_meta.query(query_embeddings=[query_GPT_embedding], n_results=5)

        return jsonify({"results": resultsGPTmeta["metadatas"][0]})

    elif ai == 'Gemini':

        start = time.time()
        response = gemini_client.models.embed_content(
            model='models/gemini-embedding-001',
            contents=query,
            config=types.EmbedContentConfig(task_type="RETRIEVAL_QUERY")
        )
        end = time.time()
        evaluateExecutionTime(model='gemini-embedding-001', start=start, end=end, query=query, implementation='GeminiEmbeddingSimple', mongo=mongoWrite)
        count = gemini_client.models.count_tokens(
            model='models/gemini-embedding-001',
            contents=query
        )
        evaluateTokenUsage(model='gemini-embedding-001', inputTokens=count.total_tokens, totalTokens=count.total_tokens, thinkingTokens=0, outputTokens=0, query=query, implementation='GeminiEmbeddingSimple', mongo=mongoWrite)

        embedding = response.embeddings[0].values

        resultsGemini = chroma_Gemini_collection.query(query_embeddings=[embedding], n_results=5)
        return jsonify({"results": resultsGemini["metadatas"][0]})

    elif ai == 'Geminimeta':

        start = time.time()
        response = gemini_client.models.embed_content(
            model='models/gemini-embedding-001',
            contents=query,
            config=types.EmbedContentConfig(task_type="RETRIEVAL_QUERY")
        )
        end = time.time()
        evaluateExecutionTime(model='gemini-embedding-001', start=start, end=end, query=query, implementation='GeminiEmbeddingStructured', mongo=mongoWrite)
        count = gemini_client.models.count_tokens(
            model='models/gemini-embedding-001',
            contents=query
        )
        evaluateTokenUsage(model='gemini-embedding-001', inputTokens=count.total_tokens, totalTokens=count.total_tokens, thinkingTokens=0, outputTokens=0, query=query, implementation='GeminiEmbeddingStructured', mongo=mongoWrite)

        embedding = response.embeddings[0].values

        resultsGeminiMeta = chroma_Gemini_collection_meta.query(query_embeddings=[embedding], n_results=5)

        return jsonify({"results": resultsGeminiMeta["metadatas"][0]})

    elif ai == 'MeiliSearch':

        start = time.time()
        search_results = searchIndex.search(query, {"limit": 5})['hits']
        end = time.time()
        evaluateExecutionTime(model='MeiliSearch', start=start, end=end, query=query, implementation='MeiliSearchBasic', mongo=mongoWrite)

        result = list()

        for sr in search_results:
            res = {
                "id": sr['id'],
                "name": sr['name'],
                "category": sr['category'],
                "description": sr['description'],
                "docs": sr['docs'],
                "https": sr['https'],
                "cors": sr['cors'],
                "authentication": sr['authentication'],
                "type": sr['type']
            }

            result.append(res)

        return jsonify({"results": result})

    elif ai == 'MeiliSearchEmm':

        start = time.time()
        search_results = searchIndexEmm.search(query, {
            "hybrid": {
                "embedder": "default",
                "semanticRatio": 0.4
            },
            "limit": 5})['hits']
        end = time.time()
        evaluateExecutionTime(model='MeiliSearch', start=start, end=end, query=query, implementation='MeiliSearchHybrid', mongo=mongoWrite)



        evaluateTokenUsage(model='text-embedding-3-small', inputTokens=countTokensMeiliSearchHybrid(query), totalTokens=countTokensMeiliSearchHybrid(query), thinkingTokens=0, outputTokens=0, query=query, implementation='MeiliSearchHybrid',
                           mongo=mongoWrite)

        result = list()

        for sr in search_results:
            res = {
                "id": sr['id'],
                "name": sr['name'],
                "category": sr['category'],
                "description": sr['description'],
                "docs": sr['docs'],
                "https": sr['https'],
                "cors": sr['cors'],
                "authentication": sr['authentication'],
                "type": sr['type']
            }

            result.append(res)

        return jsonify({"results": result})

    elif ai == 'GPTprompt':
        data = databaseQuerySearchGPT(query, mongoWrite)
        return jsonify({"results": data})

    elif ai == 'Geminiprompt':
        data = databaseQuerySearchGemini(query, mongoWrite)
        return jsonify({"results": data})

    elif ai == 'GPTdesc':

        start = time.time()
        OpenAIresponse = OpenAI_client.embeddings.create(model="text-embedding-3-large", input=query)
        end = time.time()
        evaluateExecutionTime(model='text-embedding-3-large', start=start, end=end, query=query, implementation='OpenAIEmbeddingDescriptive', mongo=mongoWrite)
        evaluateTokenUsage(model=OpenAIresponse.model, inputTokens=OpenAIresponse.usage.prompt_tokens, totalTokens=OpenAIresponse.usage.total_tokens, thinkingTokens=0, outputTokens=0, query=query, implementation='OpenAIEmbeddingDescriptive', mongo=mongoWrite)

        query_GPT_embedding = OpenAIresponse.data[0].embedding
        resultsGPTdesc = chroma_GPT_collection_desc.query(query_embeddings=[query_GPT_embedding], n_results=5)

        return jsonify({"results": resultsGPTdesc["metadatas"][0]})

    elif ai == 'Geminidesc':

        start = time.time()
        response = gemini_client.models.embed_content(
            model='models/gemini-embedding-001',
            contents=query,
            config=types.EmbedContentConfig(task_type="RETRIEVAL_QUERY")
        )
        end = time.time()
        evaluateExecutionTime(model='gemini-embedding-001', start=start, end=end, query=query, implementation='GeminiEmbeddingDescriptive', mongo=mongoWrite)
        count = gemini_client.models.count_tokens(
            model='models/gemini-embedding-001',
            contents=query
        )
        evaluateTokenUsage(model='gemini-embedding-001', inputTokens=count.total_tokens, totalTokens=count.total_tokens, thinkingTokens=0, outputTokens=0, query=query, implementation='GeminiEmbeddingDescriptive', mongo=mongoWrite)

        embedding = response.embeddings[0].values

        resultsGeminiDesc = chroma_Gemini_collection_desc.query(query_embeddings=[embedding], n_results=5)

        return jsonify({"results": resultsGeminiDesc["metadatas"][0]})
    else:
        start = time.time()
        response = gemini_client.models.embed_content(
            model='models/gemini-embedding-001',
            contents=query,
            config=types.EmbedContentConfig(task_type="RETRIEVAL_QUERY")
        )
        end = time.time()
        evaluateExecutionTime(model='gemini-embedding-001', start=start, end=end, query=query,
                              implementation='GeminiEmbeddingStructured', mongo=mongoWrite)
        count = gemini_client.models.count_tokens(
            model='models/gemini-embedding-001',
            contents=query
        )
        evaluateTokenUsage(model='gemini-embedding-001', inputTokens=count.total_tokens, totalTokens=count.total_tokens,
                           thinkingTokens=0, outputTokens=0, query=query, implementation='GeminiEmbeddingStructured',
                           mongo=mongoWrite)

        embedding = response.embeddings[0].values

        resultsGeminiMeta = chroma_Gemini_collection_meta.query(query_embeddings=[embedding], n_results=5)

        return jsonify({"results": resultsGeminiMeta["metadatas"][0]})

@main_blueprint.route('/gpt-summary', methods=['POST'])
@cross_origin()
def gptSummary():
    mongoWrite = current_app.extensions["mongo_readwrite_client"]

    data = request.get_json()
    ids = data.get('ids', [])
    userQuery = data.get('searchQuery', '')

    docs = chroma_Gemini_collection_meta.get(ids=ids)

    return {'summary': compareGPT(docs, userQuery, mongoWrite)}

@main_blueprint.route('/gemini-summary', methods=['POST'])
@cross_origin()
def geminiSummary():
    mongoWrite = current_app.extensions["mongo_readwrite_client"]

    data = request.get_json()
    ids = data.get('ids', [])
    userQuery = data.get('searchQuery', '')

    docs = chroma_Gemini_collection_meta.get(ids=ids)

    return {'summary': compareGemini(docs, userQuery, mongoWrite)}

@main_blueprint.route('/selected', methods=['POST'])
@cross_origin()
def selected():
    mongoWrite = current_app.extensions["mongo_readwrite_client"]

    data = request.get_json()

    author = 'Author'
    data['evaluator'] = author

    # simple, named, complex, specific, typo
    queryType = 'named'
    data['queryType'] = queryType

    if mongo.db.searchEvaluation.find({"query":data['query'], "component": data['component'], "evaluator":author}):
        mongoWrite['api']['searchEvaluation'].delete_many({"query": data['query'], "component": data['component'], "evaluator": author})

    mongoWrite['api']['searchEvaluation'].insert_one(data)

    return {
        'status': 'success',
        'data': data
    }

@main_blueprint.route('/compare-eval', methods=['POST'])
@cross_origin()
def comparisonEvaluation():
    mongoWrite = current_app.extensions["mongo_readwrite_client"]

    data = request.get_json()

    author = 'Author'
    data['evaluator'] = author

    # simple, named, complex, specific
    queryType = 'specific'
    data['queryType'] = queryType

    mongoWrite['api']['comparisonEvaluation'].insert_one(data)


    return {
        'status': 'success',
        'data': data
    }

def getSearchSimulationDocuments(query, component, scenario="searchEvaluation"):

    if scenario == "searchEvaluation":

        evaluation = list(
            mongo.db.searchEvaluation.find({"query": query, "component": component, "evaluator": "Author"}, {"accepted": 1, "rejected": 1}).limit(2))

        if len(evaluation) != 1:
            print("Error: more than one or none document exists.")
            return None
        else:
            evaluationList = (
                    evaluation[0].get("accepted", [])
                    + evaluation[0].get("rejected", [])
            )

        ids = [ObjectId(item["id"]) for item in evaluationList]

        documents = mongo.db.apis.find({"_id": {"$in": ids}})

        # Map docs by their string ID
        documentsById = {
            str(doc["_id"]): doc
            for doc in documents
        }

        # Restore the original position
        orderedDocuments = [
            {
                **documentsById[item["id"]],
                "position": item["position"]
            }
            for item in evaluationList
            if item["id"] in documentsById
        ]

        orderedDocuments.sort(key=lambda doc: doc["position"])

        result = list()
        for doc in orderedDocuments:
            r = {
                "id": str(doc['_id']),
                "name": doc['name'],
                "category": doc['category'],
                "description": doc['description'],
                "docs": doc['docs'],
                "type": doc['type'],
                "https": doc['https'],
                "cors": doc['cors'],
                "authentication": doc['authentication'],
            }
            result.append(r)

        return result

    elif scenario == "comparisonEvaluation":
        evaluation = list(mongo.db.comparisonEvaluation.find({"query": query, "model": component, "evaluator": "Author"}, {"resultIds": 1}).limit(2))

        if len(evaluation) != 1:
            print("Error: more than one or none document exists.")
            return None
        else:
            evaluationList = evaluation[0].get("resultIds", [])

        ids = [ObjectId(item["id"]) for item in evaluationList]

        documents = mongo.db.apis.find({"_id": {"$in": ids}})

        # Map docs by their string ID
        documentsById = {
            str(doc["_id"]): doc
            for doc in documents
        }

        # Restore the original position
        orderedDocuments = [
            {
                **documentsById[item["id"]],
                "position": item["position"]
            }
            for item in evaluationList
            if item["id"] in documentsById
        ]

        orderedDocuments.sort(key=lambda doc: doc["position"])

        result = list()
        for doc in orderedDocuments:
            r = {
                "id": str(doc['_id']),
                "name": doc['name'],
                "category": doc['category'],
                "description": doc['description'],
                "docs": doc['docs'],
                "type": doc['type'],
                "https": doc['https'],
                "cors": doc['cors'],
                "authentication": doc['authentication'],
            }
            result.append(r)

        return result

    else:

        print("Invalid scenario flag: ", scenario)
        return None

@main_blueprint.route('/simulate-search')
@cross_origin()
def simulateSearch():

    query = request.args.get('q')
    ai = request.args.get('ai')

    if ai == 'GPT':

        return jsonify({"results": getSearchSimulationDocuments(query, "OpenAISimple")})

    elif ai == 'GPTmeta':

        return jsonify({"results": getSearchSimulationDocuments(query, "OpenAIStructured")})

    elif ai == 'Gemini':

        return jsonify({"results": getSearchSimulationDocuments(query, "GeminiSimple")})

    elif ai == 'Geminimeta':

        return jsonify({"results": getSearchSimulationDocuments(query, "GeminiStructured")})

    elif ai == 'MeiliSearch':

        return jsonify({"results": getSearchSimulationDocuments(query, "Meilisearch")})

    elif ai == 'MeiliSearchEmm':

        return jsonify({"results": getSearchSimulationDocuments(query, "MeilisearchEmbed")})

    elif ai == 'GPTprompt':

        return jsonify({"results": getSearchSimulationDocuments(query, "OpenAIPrompt")})

    elif ai == 'Geminiprompt':

        return jsonify({"results": getSearchSimulationDocuments(query, "GeminiPrompt")})

    elif ai == 'GPTdesc':

        return jsonify({"results": getSearchSimulationDocuments(query, "OpenAIDescriptive")})

    elif ai == 'Geminidesc':

        return jsonify({"results": getSearchSimulationDocuments(query, "GeminiDescriptive")})

    else:

        return jsonify({"results": getSearchSimulationDocuments(query, "GPT", scenario="comparisonEvaluation")})

def getSimulatedComparison(query,model):

    html = list(mongo.db.comparisonEvaluation.find({"query":query, "model":model, "evaluator":"Author"}, {"summary":1}).limit(2))

    if len(html) != 1:
        print("Error: more than one or none document exists.")
        return None
    else:
        return html[0]["summary"]


@main_blueprint.route('/simulate-gpt-summary', methods=['POST'])
@cross_origin()
def gptSimulateSummary():

    data = request.get_json()
    return {'summary': getSimulatedComparison(data['searchQuery'], 'GPT')}

@main_blueprint.route('/simulate-gemini-summary', methods=['POST'])
@cross_origin()
def geminiSimulateSummary():

    data = request.get_json()
    return {'summary': getSimulatedComparison(data['searchQuery'], 'Gemini')}

@main_blueprint.route('/simulate-selected', methods=['POST'])
@cross_origin()
def simulateSelected():
    mongoWrite = current_app.extensions["mongo_readwrite_client"]

    data = request.get_json()

    author = 'Evaluator'
    data['evaluator'] = author

    if mongo.db.simulatedSearchEvaluation.find({"query":data['query'], "component": data['component'], "evaluator":author}):
        mongoWrite['api']['simulatedSearchEvaluation'].delete_many({"query": data['query'], "component": data['component'], "evaluator": author})

    mongoWrite['api']['simulatedSearchEvaluation'].insert_one(data)

    return {
        'status': 'success',
        'data': data
    }

@main_blueprint.route('/simulate-compare-eval', methods=['POST'])
@cross_origin()
def simulateComparisonEvaluation():
    mongoWrite = current_app.extensions["mongo_readwrite_client"]

    data = request.get_json()

    author = 'Evaluator'
    data['evaluator'] = author

    mongoWrite['api']['simulatedComparisonEvaluation'].insert_one(data)


    return {
        'status': 'success',
        'data': data
    }
