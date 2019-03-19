from flask import Flask, request, current_app

from webapp import classifier


app = Flask(__name__)
app.register_blueprint(classifier.mod)

if __name__ == '__main__':
    app.run()
