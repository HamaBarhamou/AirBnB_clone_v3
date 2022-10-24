#!/usr/bin/python3
"""
states api
"""


from models import storage
from models.city import City
from api.v1.views import app_views
from flask import jsonify, request, redirect
from werkzeug.exceptions import HTTPException
import requests
from os import getenv


@app_views.route('/states/<state_id>/cities',
                 strict_slashes=False,
                 methods=['GET', 'DELETE', 'POST'])
@app_views.route('/cities/<city_id>',
                 strict_slashes=False,
                 methods=['GET', 'DELETE', 'PUT'])
def Cities(state_id=None, city_id=None):
    HBNB_API_HOST = getenv('HBNB_API_HOST')
    if request.method == 'GET':
        """x = requests.get('https://w3schools.com/python/demopage.htm')
        x = requests.get('http://'+HBNB_API_HOST+'/api/v1/states/{}'
                         .format(state_id))
        print("status code:",x.status_code)"""
        return jsonify({"msg": "Cities List all"}), 200
