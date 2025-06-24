from flask import Blueprint, jsonify, request
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


main_blueprint = Blueprint('main', __name__)

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
    # GPT()
    GPTmeta()
    return jsonify({'status': 'ChatGPT done.'})

@main_blueprint.route('/support/create_Gemini')
def createGeminiCollection():
    # GEMINI()
    GEMINImeta()
    return jsonify({'status': 'Gemini done.'})

@main_blueprint.route('/support/count_tokens')
def countTokens():
    tokens = countGPTtokens()
    tokenData = {
        'GPT_embeddings': tokens
    }
    return jsonify(tokenData)

@main_blueprint.route('/search')
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

    query_GPT_embedding = OpenAI_client.embeddings.create(model="text-embedding-ada-002", input=query).data[0].embedding
    resultsGPT = chroma_GPT_collection.query(query_embeddings=[query_GPT_embedding], n_results=5)
    resultsGPTmeta = chroma_GPT_collection_meta.query(query_embeddings=[query_GPT_embedding], n_results=5)

    query_Gemini_embedding = genai.embed_content(model=embedding_model_name, content=query)['embedding']
    resultsGemini = chroma_Gemini_collection.query(query_embeddings=[query_Gemini_embedding], n_results=5)
    resultsGeminiMeta = chroma_Gemini_collection_meta.query(query_embeddings=[query_Gemini_embedding], n_results=5)

    result = {
        "GPT_RAG": resultsGPT,
        "GPT_RAG_meta": resultsGPTmeta,
        "Gemini_RAG": resultsGemini,
        "Gemini_RAG_meta": resultsGeminiMeta,
    }

    return jsonify({"results": resultsGPT["metadatas"][0]})
