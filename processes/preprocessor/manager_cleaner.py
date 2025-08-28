from cleaner import Cleaner
from kafka_files.producer import Producer
from kafka_files.consumer import Consumer

class ManagerCleaner:

    def __init__(self, topic):
        self.topic = topic
        self.producer = Producer()
        self.consumer = Consumer(self.topic)
        self.event = self.consumer.get_consumer_events()
        self.cleaner = Cleaner()



    def consume_and_produce(self):
        for massage in self.event:
            # start cleaning end
            new_massage = self.cleaner.remove_punctuation_marks(str(massage.value.values()))
            print(new_massage)
            new_massage = self.cleaner.remove_special_characters(new_massage)
            print(new_massage)
            new_massage = self.cleaner.remove_Remove_whitespace(new_massage)
            print(new_massage)
            new_massage = self.cleaner.remove_stop_words(new_massage)
            print(new_massage)
            new_massage = self.cleaner.uppercase_to_lowercase(new_massage)
            print(new_massage)
            new_massage = self.cleaner.find_the_roots_of_words(new_massage)
            print(new_massage)



# topic = "anti"
# m = ManagerCleaner(topic)
# m.consume_and_produce()
