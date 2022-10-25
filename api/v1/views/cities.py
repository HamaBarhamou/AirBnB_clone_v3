#!/usr/bin/python3
"""
states api
"""


from os import abort
from models import storage
from models.city import City
from models.state import State
from api.v1.views import app_views
from flask import jsonify, abort
from werkzeug.exceptions import HTTPException


@app_views.route('/states/<state_id>/cities',
                 strict_slashes=False,
                 methods=['GET'])
def getCities(state_id):
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    tab = []
    cities = storage.all(City).values()
    for c in cities:
        if c.state_id == state_id:
            tab.append(c.to_dict())

    return tab, 200


@app_views.route('/states/<state_id>/cities',
                 strict_slashes=False,
                 methods=['POST'])
def creatCitie(state_id):
    pass


@app_views.route('/states/<state_id>/cities',
                 strict_slashes=False,
                 methods=['DELETE'])
def delCitie(state_id):
    pass


@app_views.route('/cities/<city_id>',
                 strict_slashes=False,
                 methods=['GET'])
def getCitieById(city_id):
    citie = storage.get(City, city_id)
    if citie is None:
        abort(404)

    return jsonify(citie.to_dict()), 200
