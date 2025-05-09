from bson import ObjectId
from datetime import datetime
import json
from ..extensions import mongo

class BaseModel:
    """Base model class for MongoDB documents."""

    collection_name = None  # Override this in subclasses

    def __init__(self, **kwargs):
        # Set attributes from kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)

        # Set default values if not provided
        if not hasattr(self, '_id'):
            self._id = None

        if not hasattr(self, 'created_at'):
            self.created_at = datetime.now()

        if not hasattr(self, 'updated_at'):
            self.updated_at = datetime.now()

    @classmethod
    def get_collection(cls):
        """Get MongoDB collection."""
        # mongo = current_app.extensions['pymongo'].db
        # return mongo[cls.collection_name]
        return mongo.db[cls.collection_name]

    def save(self):
        """Save document to MongoDB."""
        collection = self.get_collection()

        # Update timestamp
        self.updated_at = datetime.now()

        if self._id is not None:
            # Update existing document
            doc = self.to_dict()
            if '_id' in doc:
                del doc['_id']

            result = collection.update_one(
                {'_id': ObjectId(self._id) if isinstance(self._id, str) else self._id},
                {'$set': doc}
            )
            return result.modified_count > 0
        else:
            # Insert new document
            self._id = ObjectId()
            doc = self.to_dict()
            result = collection.insert_one(doc)
            return result.acknowledged

    def delete(self):
        """Delete document from MongoDB."""
        if not self._id:
            return False

        collection = self.get_collection()
        result = collection.delete_one({'_id': ObjectId(self._id)})
        return result.deleted_count > 0

    def to_dict(self):
        """Convert model to dictionary."""
        # Get all attributes
        doc = {k: v for k, v in self.__dict__.items() if not k.startswith('_') or k == '_id'}

        return doc

    def to_json(self):
        """Convert model to JSON string."""
        return json.dumps(self.to_dict(), default=str)

    @classmethod
    def find_by_id(cls, id):
        """Find document by ID."""
        if not id:
            return None

        collection = cls.get_collection()
        doc = collection.find_one({'_id': ObjectId(id)})

        if not doc:
            return None

        return cls(**doc)

    @classmethod
    def find_all(cls):
        """Find all documents."""
        collection = cls.get_collection()
        docs = collection.find()
        return [cls(**doc) for doc in docs]

    @classmethod
    def find(cls, query=None, sort=None, limit=None, skip=None):
        """Find documents with query."""
        collection = cls.get_collection()
        cursor = collection.find(query or {})

        if sort:
            cursor = cursor.sort(sort)

        if skip:
            cursor = cursor.skip(skip)

        if limit:
            cursor = cursor.limit(limit)

        return [cls(**doc) for doc in cursor]