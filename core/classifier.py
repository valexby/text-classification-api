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
    def __init__(self, model=None):
        self.model = model

    def load(self, model_path):
        with open(model_path, 'rb') as model_file:
            self.model = pickle.load(model_file)
        self.model.steps[0][1].tokenizer = Stemmer()

    def dump(self, model_path):
        self.model.steps[0][1].tokenizer = None
        with open(model_path, 'wb') as model_file:
            pickle.dump(self.model, model_file)

    def predict(self, text):
        predicted = self.model.predict([text])
        return int(predicted[0])
