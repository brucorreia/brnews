import os
import pymongo

class MongoDBInteractor:
    def __init__(self):

        host = os.getenv('MONGO_HOST', 'mongo')
        port = int(os.getenv('MONGO_PORT', 27017))
        database = os.getenv('MONGO_DB', 'news_db')
        collection = os.getenv('MONGO_COLLECTION', 'news_collection')
        
        self.client = pymongo.MongoClient(host, port)
        self.db = self.client[database]
        self.collection = self.db[collection]

    def insert(self, payload):
        self.collection.insert_one(payload)
        return True

    def get(self, payload):
        result = self.collection.find_one(payload)
        return result is not None
