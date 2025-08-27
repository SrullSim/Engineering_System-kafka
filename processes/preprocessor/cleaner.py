import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class Cleaner:

    def __init__(self):
        self.text = None

    @staticmethod
    def remove_punctuation_marks(text):
        clean_text = text
        for c in string.punctuation:
            clean_text = clean_text.replace(c, "")
        return clean_text


    @staticmethod
    def remove_special_characters(text):
        clean_text = text.translate(str.maketrans('', '', string.punctuation))
        return clean_text

    @staticmethod
    def remove_Remove_whitespace(text):
        clean_text = re.sub(r'\s+', ' ', text).strip()
        return clean_text

    @staticmethod
    def uppercase_to_lowercase(text):
        return text.lower()


    @staticmethod
    def remove_stop_words(text):
        pass


# test_text = " self. the #    # m  and with for about  kdir & git % in @ OPen? "
# c = Cleaner
