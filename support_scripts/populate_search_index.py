import meilisearch
import os
from dotenv import load_dotenv
from app.extensions import mongo

load_dotenv()

MEILISEARCH_SECRET = os.environ['MEILISEARCH_SECRET']
MEILISEARCH_INDEX = os.environ['MEILISEARCH_INDEX']

searchClient = meilisearch.Client('http://127.0.0.1:7700', MEILISEARCH_SECRET)
searchIndex = searchClient.index(MEILISEARCH_INDEX)
documents = list()

def populate_search_index():

    apis = mongo.db.apis.find()

    for api in apis:

        doc = {
            'id': str(api['_id']),
            'name': api['name'],
            'description': api['description'],
            'api_keywords': api['api_keywords'],
        }
        documents.append(doc)

    searchIndex.add_documents(documents)

    searchIndex.update_filterable_attributes(['name', 'description', 'api_keywords'],)

    return
