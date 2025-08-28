import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer



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
    def remove_stop_words(text):
        nltk.download('stopwords', quiet=True)
        nltk.download('punkt_tab', quiet=True)
        stop_words = set(stopwords.words('english'))
        tokens = word_tokenize(text.lower())
        filtered_tokens = [word for word in tokens if word not in stop_words]

        return  " ".join(filtered_tokens)


    @staticmethod
    def find_the_roots_of_words(text):
        ps = PorterStemmer()
        words = word_tokenize(text)
        stemmed_words = [ps.stem(word) for word in words]
        return ' '.join(stemmed_words)


    @staticmethod
    def uppercase_to_lowercase(text):
        return text.lower()


# test_text = (" self. the #    # m  and with for about  kdir & git % in @ OPen?"
#              "Programmers program with programming languages ")
# c = Cleaner
# print(c.find_the_roots_of_words(test_text))
