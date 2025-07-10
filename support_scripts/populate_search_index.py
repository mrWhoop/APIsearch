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

def cleanUp():
    try:
        index = searchClient.index(MEILISEARCH_INDEX)

        # Delete all documents
        task = index.delete_all_documents()
        print(f"Deleting all documents from '{MEILISEARCH_INDEX}' index...")

        # Wait for the task to complete
        searchClient.wait_for_task(task['taskUid'])

        print(f"All documents deleted from '{MEILISEARCH_INDEX}' index successfully!")
        return True
    except Exception as e:
        print(f"Error clearing documents from index '{MEILISEARCH_INDEX}': {e}")
        return False

def populate_search_index():

    cleanUp()

    apis = mongo.db.apis.find()

    for api in apis:

        doc = {
            'id': str(api['_id']),
            'name': api['name'],
            'description': api['description'],
            'category': api['category'],
            'docs': api['docs'],
            'api_keywords': api['api_keywords'],
        }
        documents.append(doc)

    searchIndex.add_documents(documents)

    searchIndex.update_filterable_attributes(['name', 'description', 'api_keywords'],)

    return
