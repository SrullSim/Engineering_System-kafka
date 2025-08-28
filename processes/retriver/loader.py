import time

import pymongo

from dal_mongo.dal import MongoDAL
import pandas as pd
from kafka_files.producer import Producer

class Loader:
    def __init__(self,uri , db):
        self.db = db
        self.connection = MongoDAL(uri, db)
        self.collection = self.connection.collection
        self.oldest = 0
        self.massages = 0

    # Retrieves the 100 oldest timestamped entries
    def pull_massages_by_time(self, time_stamp, dict_origin_target, category):
        try:
            run = True
            while run:
                if  self.oldest is None:
                    massages = self.collection.find().sort(time_stamp,pymongo.ASCENDING).limit(100)
                    self.oldest += 100
                    self.massages = massages
                    if not  massages:
                        run = False
                else:
                    massages = self.collection.find().sort(time_stamp, pymongo.ASCENDING).limit(100).skip(self.oldest)
                    self.oldest += 100
                    self.massages = massages
                    if not  massages:
                        run = False
                for massage in massages:
                    self.publish_massage(dict_origin_target[massage[category]], list(massage))
                    print(massage)
                time.sleep(60)

        except:
            return None

    def publish_massage(self, topic, massage):
        producer = Producer().publish_message(topic, massage)


