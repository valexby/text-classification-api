import logging
import json

from flask import Blueprint, request
from core.classifier import Classifier


logger = logging.getLogger(__name__)


mod = Blueprint('classifier', __name__)

classifier = Classifier()
classifier.load('./data/model.pk')

@mod.route("/", methods=('POST',))
def classify():
    text = request.json['text']
    print('kek')
    logger.info("Get classification request for %s. Predicting class...", text)
    text_class = classifier.predict(text)
    logger.info("Set $s class for %s. Sending response...", text_class, text)
    print('lol')
    return json.dumps({'data': text_class})
