#!/usr/bin/python3
"""
states api
"""


from sqlalchemy import values
from models import storage
from models.state import State
from api.v1.views import app_views
from flask import jsonify, request, redirect, abort
from werkzeug.exceptions import HTTPException


@app_views.route('/states', strict_slashes=False, methods=['GET'])
def getState():
    states = storage.all(State).values()
    liste = []
    for loop in states:
        liste.append(loop.to_dict())
    return liste, 200


@app_views.route('/states', strict_slashes=False, methods=['POST'])
def creatState():
    data = request.get_json()

    if type(data) is not dict:
        abort(404, "Not a JSON")
    if "name" not in data:
        abort(400, "Missing name")
    state = State(**data)
    storage.new(state)
    storage.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>',
                 strict_slashes=False, methods=['GET'])
def getStateById(state_id):
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>',
                 strict_slashes=False, methods=['DELETE'])
def delSate(state_id):
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states/<state_id>', strict_slashes=False, methods=['PUT'])
def updateState(state_id):
    data = request.get_json()

    if type(data) is not dict:
        abort(404, "Not a JSON")
    if "name" not in data:
        abort(400, "Missing name")

    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    black_list = ["id", "created_at", "updated_at"]
    for key, value in data.items():
        if key not in black_list:
            setattr(state, key, value)
    storage.save()
    return jsonify(state.to_dict()), 200
