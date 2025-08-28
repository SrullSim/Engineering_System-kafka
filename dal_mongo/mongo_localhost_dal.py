from pymongo import MongoClient

class MongoDALLocalhost:
    def __init__(self,host="localhost", port=27027, db_name=None, collection=None):
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]
        self.collection = self.db[collection]

    def get_collection(self):

        return list(self.collection.find({ }))

    def add_document(self, message):
        self.collection.insert_one(message)
        return {"status": "success", "message": "added"}

    def get_value(self, field):
        return list(self.collection.find_one({}, {field:1}))

    def length_collection(self):
        return self.collection.count_documents({})