from pymongo import MongoClient


class MongoDAL:
    def __init__(self,uri , db_name, collection_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def get_collection(self):

        return list(self.collection.find({ }))

    def add_document(self, message):
        self.collection.insert_one(message)
        return {"status": "success", "message": "added"}

    def length_collection(self):
        return self.collection.count_documents({})


