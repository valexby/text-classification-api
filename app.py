import logging
import json

from flask import Flask, request, current_app
from classifier import Classifier


logger = logging.getLogger(__name__)

app = Flask(__name__)
classifier = Classifier()
classifier.load('./data/model.pk')
app.classifier = classifier

@app.route("/", methods=('POST',))
def classify():
    import os
    print(os.listdir('/usr/local/share/nltk_data'))
    print(os.listdir('/usr/local/share/nltk_data/tokenizers/punkt/PY3'))
    text = request.json['text']
    logger.info("Get classification request for %s. Predicting class...", text)
    text_class = current_app.classifier.predict(text)
    logger.info("Set $s class for %s. Sending response...", text_class, text)
    return json.dumps({'data': text_class})


if __name__ == '__main__':
    app.run()
