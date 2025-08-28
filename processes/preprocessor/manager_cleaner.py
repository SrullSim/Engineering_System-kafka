from cleaner import Cleaner
from kafka_files.producer import Producer
from kafka_files.consumer import Consumer

class ManagerKafka:

    def __init__(self, topic):
        self.topic = topic
        self.producer = Producer()
        self.consumer = Consumer(self.topic)
        self.event = self.consumer.get_consumer_events()
        self.cleaner = Cleaner()

    def consume_and_produce(self):
        for massage in self.event.value():
            self.cleaner.remove_punctuation_marks()

