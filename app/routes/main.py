from flask import Blueprint, jsonify
from ..extensions import mongo
from support_scripts.populate_database import populate_database
from support_scripts.populate_search_index import populate_search_index
from app.models.api import Api, EndPoint

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/populate_database')
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


@main_blueprint.route('/search')
def search():

    return None
