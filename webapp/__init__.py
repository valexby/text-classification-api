from flask import Flask, request, current_app

from webapp import classifier
from webapp.security import authenticate_request

def create_app():
    app = Flask(__name__)

    app.register_blueprint(classifier.mod)
    register_authentication_handler(app)
    return app

def register_authentication_handler(app):
    @app.before_request
    def before_request():
        authentication_challenge = authenticate_request()
        if authentication_challenge:
            return authentication_challenge
