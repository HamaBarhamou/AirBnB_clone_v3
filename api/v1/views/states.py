#!/usr/bin/python3
"""
states api
"""

from models import storage
from models.state import State
from api.v1.views import app_views_states
from flask import jsonify, request, redirect
from werkzeug.exceptions import HTTPException

@app_views_states.route('/states',
                        strict_slashes=False, 
                        methods = ['GET'])
@app_views_states.route('/states/<state_id>',
                        strict_slashes=False, 
                        methods = ['POST', 'GET'])
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
            return jsonify({"error": "Not found"}), '404'

        return result
    
    if request.method == 'POST':
        return jsonify({"states": "POST methode"})
