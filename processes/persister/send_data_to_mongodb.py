from dal_mongo.mongo_localhost_dal import MongoDALLocalhost
from kafka_files.consumer import Consumer

class PushToMongodb:
    def __init__(self, topic,host , port , db_name , collection ):
        self.topic = topic
        self.mongo_connection = MongoDALLocalhost(host, port, db_name, collection)

    def push(self):
        consumer = Consumer(self.topic).get_consumer_events()
        for massage in consumer:
            self.mongo_connection.add_document(massage)