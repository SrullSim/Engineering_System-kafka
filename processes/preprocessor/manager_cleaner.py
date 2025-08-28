from cleaner import Cleaner
from kafka_files.producer import Producer
from kafka_files.consumer import Consumer
from config.config import TOPIC_INPUT_CLEANER_ANTISEMITIC
from config.config import TOPIC_OUTPUT_CLEANER_ANTISEMITIC

class ManagerCleaner:

    def __init__(self, topic):
        self.topic = topic
        self.producer = Producer()
        self.consumer = Consumer(self.topic)
        self.event = self.consumer.get_consumer_events()
        self.cleaner = Cleaner()
        self.topic_output =



    def consume_and_produce(self):
        for massage in self.event:
            # start cleaning end preparing
            new_massage = self.cleaner.remove_punctuation_marks(str(massage.value.values()))
            new_massage = self.cleaner.remove_special_characters(new_massage)
            new_massage = self.cleaner.remove_Remove_whitespace(new_massage)
            new_massage = self.cleaner.remove_stop_words(new_massage)
            new_massage = self.cleaner.uppercase_to_lowercase(new_massage)
            new_massage = self.cleaner.find_the_roots_of_words(new_massage)

            self.producer.publish_message(,{"clean_text":new_massage})



# topic = "anti"
# m = ManagerCleaner(topic)
# m.consume_and_produce()
