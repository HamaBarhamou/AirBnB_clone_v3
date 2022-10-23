#!/usr/bin/python3
"""
states api
"""

from unicodedata import name

from sqlalchemy import values
from models import storage
from models.state import State
from api.v1.views import app_views_states
from flask import jsonify, request, redirect
from werkzeug.exceptions import HTTPException

@app_views_states.route('/states',
                        strict_slashes=False, 
                        methods = ['GET', 'POST'])
@app_views_states.route('/states/<state_id>',
                        strict_slashes=False, 
                        methods = ['PUT', 'GET', 'DELETE'])
def states(state_id=None,):
    if request.method == 'GET':
        reponse = storage.all(State).values()
        result = []
        for loop in reponse:
            r = loop.to_dict()
            dic = {}
            dic['__class__'] = r['__class__']
            dic['created_at'] = r['created_at']
            dic['id'] = r['id']
            dic['name'] = r['name']
            dic['updated_at'] = r['updated_at']
            result.append(dic)

        if state_id is not None:
            for loop in result:
                if state_id == loop['id']:
                    return loop
            return jsonify({"error": "Not found"}), 404

        return result
    
    if request.method == 'POST':
        data = request.get_json()

        if type(data) is not dict:
            return jsonify({"error": "Not a JSON"}), 400
        if "name" not in data:
            return jsonify({"error": "Missing name"}), 400

        obj = State(name=data['name'])
        
        storage.new(obj)
        storage.save()

        return jsonify(obj.to_dict()), 201

    if request.method == 'DELETE':
        reponse = storage.all(State).values()
        for loop in reponse:
            if state_id == loop.to_dict()["id"]:
                storage.delete(loop)
                storage.save()
                return jsonify({}), 200

        return jsonify({"error": "Not found"}), 404

    if request.method == 'PUT':
        data = request.get_json()

        if type(data) is not dict:
            return jsonify({"error": "Not a JSON"}), 400
        if "name" not in data:
            return jsonify({"error": "Missing name"}), 400
            
        reponse = storage.all(State).values()
        state = None
        for loop in reponse:
            if state_id == loop.id:
                state = loop
                break
        if state == None:
            return jsonify({"error": "Not found"}), 404
        
        state.name = data['name']
        storage.save()
        print(state.name)

        return jsonify(state.to_dict()), 200