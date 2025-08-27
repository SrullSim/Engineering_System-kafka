from producer import Producer
from consumer import Consumer


class ManagerKafka:

    def __init__(self, topic):
        self.topic = topic
        self.producer = Producer()
        self.consumer = Consumer(self.topic)
        self.event = self.consumer.get_consumer_events()


    def consume_and_produce(self):
        for massage in self.event:
            pass


