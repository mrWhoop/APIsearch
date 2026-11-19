from flask import Flask
from .extensions import mongo
from pymongo import MongoClient
from .routes.main import main_blueprint
from flask_cors import CORS

def create_app():
    global mongo_readwrite_client

    app = Flask(__name__)

    CORS(app, origins="*")

    # Load configuration
    app.config.from_object('config.Config')

    # Initialize MongoDB connection
    mongo.init_app(app)

    app.extensions["mongo_readwrite_client"] = MongoClient(
        app.config["MONGO_READWRITE_URI"]
    )

    # Register blueprints
    app.register_blueprint(main_blueprint)

    return app
