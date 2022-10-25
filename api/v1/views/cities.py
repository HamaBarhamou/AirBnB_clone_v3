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


"""@app_views.route('/states/<state_id>/cities',
                 strict_slashes=False,
                 methods=['GET', 'DELETE', 'POST'])
@app_views.route('/cities/<city_id>',
                 strict_slashes=False,
                 methods=['GET', 'DELETE', 'PUT'])
def Cities(state_id=None, city_id=None):
    if state_id is not None:
        state = storage.get(State, state_id)
        if state is None:
            return jsonify({"error": "Not found"}), 404

    if request.method == 'GET':
        cities = storage.all(City)
        #print(state.to_dict())
        print(cities)
        tab=[]
        for city in cities:
            pass
        return jsonify({"msg": "Cities List all"}), 200

    if request.method == 'POST':
        data = request.get_json()
        if type(data) is not dict:
            return jsonify({"error": "Not a JSON"}), 400
        if "name" not in data:
            return jsonify({"error": "Missing name"}), 400

        obj = City(name=data['name'], state_id=state_id)

        storage.new(obj)
        storage.save()

        return jsonify(obj.to_dict()), 201"""

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