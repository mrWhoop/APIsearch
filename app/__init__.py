from flask import Flask
from .extensions import mongo
from .routes.main import main_blueprint

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object('config.Config')

    # Initialize MongoDB connection
    mongo.init_app(app)

    # Register blueprints
    app.register_blueprint(main_blueprint)

    return app
