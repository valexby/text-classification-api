import logging
import json

from flask import Blueprint
from core.classifier import Classifier


logger = logging.getLogger(__name__)

mod = Blueprint('general', __name__)

classifier = Classifier()
classifier.load('./data/model.pk')
mod.classifier = classifier

@mod.route("/", methods=('POST',))
def classify():
    import os
    print(os.listdir('/usr/local/share/nltk_data'))
    print(os.listdir('/usr/local/share/nltk_data/tokenizers/punkt/PY3'))
    text = request.json['text']
    logger.info("Get classification request for %s. Predicting class...", text)
    text_class = current_app.classifier.predict(text)
    logger.info("Set $s class for %s. Sending response...", text_class, text)
    return json.dumps({'data': text_class})
