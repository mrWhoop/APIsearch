from flask import Blueprint, jsonify
from ..extensions import mongo
from support_scripts.populate_database import populate_database
from app.models.api import Api, EndPoint

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/populate_database')
def populate_database_call():

    if mongo.db.apis.count_documents({}) > 0:
        mongo.db.apis.delete_many({})
        populate_database()
        apis = mongo.db.apis.find()
    else:
        populate_database()
        apis = mongo.db.apis.find()

    return jsonify(apis)


@main_blueprint.route('/search')
def populate_database_call():

    
