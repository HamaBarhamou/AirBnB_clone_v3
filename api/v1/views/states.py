#!/usr/bin/python3
"""
states api
"""

from models import storage
from models.state import State
from api.v1.views import app_views_states
from flask import jsonify, request

@app_views_states.route('/states', strict_slashes=False, 
                        methods = ['POST', 'GET'])
def states():
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
        for loop in result:
            print(loop)
        return result
    
    if request.method == 'POST':
        return jsonify({"states": "POST methode"})