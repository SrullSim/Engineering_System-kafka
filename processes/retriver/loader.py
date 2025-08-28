import time

from dal_mongo.dal import MongoDAL
import pandas as pd
from kafka_files.producer import

class Loader:
    def __init__(self,uri , db_name, collection_name):
        self.collection = MongoDAL(uri, db_name, collection_name).get_collection()
        self.oldest = None
        self.massages = None

    # Retrieves the 100 oldest timestamped entries
    def pull_massages_by_time(self, time_stamp):
        try:
            run = True
            while run:
                if  self.oldest is None:
                    massages = self.collection.find().sort(time_stamp).limit(100)
                    self.oldest += 100
                    self.massages = massages
                    if not  massages:
                        run = False
                else:
                    massages = self.collection.find().sort(time_stamp).limit(100).skip(self.oldest)
                    self.oldest += 100
                    self.massages = massages
                    if not  massages:
                        run = False
                time.sleep(6000)
        except:
            return None

    def publish_massage(self, topic):
        producer =



