#!/usr/bin/python3
"""
states api
"""

from models import storage
from models.state import State
from api.v1.views import app_views_states
from flask import jsonify, request

@app_views_states.route('/states/', strict_slashes=False, 
                        methods = ['POST', 'GET'])
def states():
    if request.method == 'GET':
        return jsonify({"states": "GET methode"})
    
    if request.method == 'POST':
        return jsonify({"states": "POST methode"})