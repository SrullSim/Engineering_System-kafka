from pymongo import MongoClient


class MongoDAL:
    def __init__(self, host="localhost", port=27017, db_name=None, collection_name=None):
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def get_collection(self):

        return list(self.collection.find())

    def add_document(self, message):
        self.collection.insert_one(message)
        return {"status": "success", "message": "added"}

