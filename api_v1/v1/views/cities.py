#!/usr/bin/python3
"""
cities api
"""


from models import storage
from models.city import City
from models.state import State
from api.v1.views import app_views
from flask import jsonify, abort, request


@app_views.route('/states/<state_id>/cities',
                 strict_slashes=False,
                 methods=['GET'])
def getCities(state_id):
    """Returns JSON cities in a given state"""
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
    """create a Citie"""
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


@app_views.route('cities/<city_id>',
                 strict_slashes=False,
                 methods=['PUT'])
def updateCitie(city_id):
    """Update a cities"""
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


@app_views.route('/cities/<city_id>',
                 strict_slashes=False,
                 methods=['DELETE'])
def delCitie(city_id):
    """Delette a cities"""
    citie = storage.get(City, city_id)

    if citie is None:
        abort(404)

    storage.delete(citie)
    storage.save()

    return jsonify({}), 200


@app_views.route('/cities/<city_id>',
                 strict_slashes=False,
                 methods=['GET'])
def getCitieById(city_id):
    """get citie by id"""
    citie = storage.get(City, city_id)
    if citie is None:
        abort(404)

    return jsonify(citie.to_dict()), 200
