from flask_pymongo import PyMongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize MongoDB connection
mongo = PyMongo()
