#!/usr/bin/python3
"""
states api
"""


from os import abort, stat
from models import storage
from models.city import City
from models.state import State
from api.v1.views import app_views
from flask import jsonify, abort, request
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
def createCitie(state_id):
    data = request.get_json()
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if type(data) is not dict:
        return jsonify({"error": "Not a JSON"}), 404
    if "name" not in data:
        return jsonify({"error": "Missing name"}), 400

    citie = City(**data)
    citie.state_id = state_id
    storage.new(citie)
    storage.save()

    return jsonify(citie.to_dict()), 200


@app_views.route('/states/cities/<city_id>',
                 strict_slashes=False,
                 methods=['PUT'])
def updateCitie(city_id):
    data = request.get_json()
    if type(data) is not dict:
        return jsonify({"error": "Not a JSON"}), 404

    citie = storage.get(City, city_id)
    if citie is None:
        abort(404)

    black_list = ["id", "created_at", "updated_at"]
    
    for key, values in data.items():
        if key not in black_list:
            setattr(citie, key, values)

    storage.save()
    
    return jsonify(citie.to_dict()), 200


@app_views.route('/states/<state_id>/cities',
                 strict_slashes=False,
                 methods=['DELETE'])
def delCitie(state_id):
    """comment"""
    pass


@app_views.route('/cities/<city_id>',
                 strict_slashes=False,
                 methods=['GET'])
def getCitieById(city_id):
    citie = storage.get(City, city_id)
    if citie is None:
        abort(404)

    return jsonify(citie.to_dict()), 200
