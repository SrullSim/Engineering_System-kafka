from pymongo import MongoClient


class MongoDAL:
    def __init__(self,uri , db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collections = self.db.list_collection_names()
        self.collection = self.db[self.collections[0]]

    def get_collection(self):

        return list(self.collection.find({ }))

    def add_document(self, message):
        self.collection.insert_one(message)
        return {"status": "success", "message": "added"}

    def get_value(self, field):
        return list(self.collection.find_one({}, {field:0}))

    def length_collection(self):
        return self.collection.count_documents({})


