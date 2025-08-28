from enricher import Enricher
from kafka_files.producer import Producer
from kafka_files.consumer import Consumer
from processes.preprocessor.cleaner import Cleaner
from config.config import TOPIC_OUTPUT_CLEANER_ANTISEMITIC
from config.config import TOPIC_OUTPUT_ENRICHER_ANTISEMITIC
from config.config import TOPIC_OUTPUT_ENRICHER_NOT_ANTISEMITIC
from config.config import OUTPUT_COLUMNS
import datetime

class ManagerEnricher:

    def __init__(self, topic):
        self.input_topic = topic
        self.producer = Producer()
        self.consumer = Consumer(self.input_topic)
        self.event = self.consumer.get_consumer_events()
        self.enricher = Enricher(self.event)




    def enrich_the_massage(self):
        for massage in self.event:

            # get the collection from the topic
            collection = self.enricher.get_json()

            if self.input_topic == TOPIC_OUTPUT_CLEANER_ANTISEMITIC:
                self.producer.publish_message(TOPIC_OUTPUT_ENRICHER_ANTISEMITIC, collection)
            else:
                self.producer.publish_message(TOPIC_OUTPUT_ENRICHER_NOT_ANTISEMITIC, collection)

