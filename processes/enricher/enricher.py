from nltk.sentiment import SentimentIntensityAnalyzer
from processes.preprocessor.cleaner import Cleaner
from config.config import WEAPONS_FILE_PATH, TOPIC_OUTPUT_CLEANER_ANTISEMITIC
import pandas as pd
import re
import json
import datetime
from kafka_files import consumer,producer


class Enricher:

    def __init__(self, event ):
        self.data = self.bring_data(event)
        self.DF = pd.DataFrame(self.data)
        self.blacklist = self.get_blacklist()
        self.topic = self.set_topic(event)

    def set_topic(self,event):
        for massage in event:
            return massage.topic

    def get_clean_text(self, event):
        for massage in event:
            text = str(massage.value["clean_text"].values())
            return text

    def get_original_text(self, event):
        for massage in event:
            text = str(massage.value["original_text"].values())
            return text

    def get_text_from_df(self,row):
        text = self.DF["original_text"]
        return text

    def bring_data(self, event):
        for massage in event:
            data = massage.value
            return json.loads(data)

    def get_blacklist(self):
        with open(WEAPONS_FILE_PATH) as file:
            lines = [line.rstrip().lower() for line in file]
        return lines

    def find_time_relevant(self, text):

        match = re.search(r'\b\d{2}-\d{2}-\d{4}\b', text)
        if match:
            return match.group(0)
        return None

    def find_weapons(self, weapons_list, text):
        weapons_detected = []
        text_list = text.split(" ")
        for weapon in text_list:
            if weapon in weapons_list:
                weapons_detected.append(weapon)
        return weapons_detected

    def score_text_sentiment(self, text):
        score = SentimentIntensityAnalyzer().polarity_scores(text)
        return score["compound"]

    def score_sentiment_to_df(self, score):
        """ score the sentiment according the score given"""
        if 1 < score > 0.5 :
            return "positive"
        elif -0.49 < score > 0.49:
            return "natural"
        elif -1 < score < -0.5:
            return "negative"
        return None

    def get_category(self):
        if self.topic == TOPIC_OUTPUT_CLEANER_ANTISEMITIC:
            return 1
        else:
            return 0

    def get_timestamp(self):
        time = datetime.datetime.now()
        return time


    def get_json(self):
        objects_list = []
        for index, row in self.DF.iterrows():
            my_dict = {}
            text = self.get_text_from_df(row)
            clean_text = self.get_clean_text(text)
            my_dict["id"] = str(row["_id"])
            my_dict["createdate"] = self.get_timestamp()
            my_dict["antisemietic"] = self.get_category()
            my_dict["original_text"] = self.get_original_text(text)
            my_dict["clean_text"] = self.get_clean_text(text)
            score = self.score_text_sentiment(clean_text)
            my_dict["sentiment"] = self.score_sentiment_to_df(score)
            my_dict["weapons_detected"] = self.find_weapons(self.get_blacklist(), clean_text)
            objects_list.append(my_dict)
        return objects_list







