from flask import Blueprint, jsonify
from ..extensions import mongo
from support_scripts.populate_database import populate_database
from support_scripts.populate_search_index import populate_search_index
from support_scripts.create_chroma_chatGPT_embeddings import createCollection
from support_scripts.countTokens import countGPTtokens
from app.models.api import Api, EndPoint

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
    createCollection()
    return jsonify({'status': 'Done.'})

@main_blueprint.route('/support/count_tokens')
def countTokens():
    tokens = countGPTtokens()
    tokenData = {
        'GPT_embeddings': tokens
    }
    return jsonify(tokenData)

@main_blueprint.route('/search')
def search():

    return None
