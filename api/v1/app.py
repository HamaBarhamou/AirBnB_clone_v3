#!/usr/bin/python3
"""
starts a Flask web application
"""

from email import message
from operator import imod
from flask import Flask
from api.v1.views import app_views
from models import *
from os import getenv
from flask import jsonify, make_response
from werkzeug.exceptions import HTTPException


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


@app.errorhandler(HTTPException)
def no_found(e):
    return jsonify({"error": "Not found"}), e.code


if __name__ == '__main__':

    api_host = getenv('HBNB_API_HOST', default='0.0.0.0')
    api_port = getenv('HBNB_API_PORT', default=5000)
    app.run(host=api_host, port=int(api_port), threaded=True)
