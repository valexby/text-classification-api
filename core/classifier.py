import pickle

from nltk import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline

class Stemmer:
    def __init__(self):
        self.stemmer = SnowballStemmer('english').stem

    def __call__(self, text):
        return [self.stemmer(i) for i in word_tokenize(text)]

class Classifier:
    def load(self, model_path):
        with open(model_path, 'rb') as model_file:
            self.model = pickle.load(model_file)

    def predict(self, text):
        predicted = self.model.predict([text])
        return int(predicted[0])
