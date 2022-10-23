#!/usr/bin/python3
"""
states api
"""

from models import storage
from models.state import State
from api.v1.views import app_views_states
from flask import jsonify

@app_views_states.route('/states/', strict_slashes=False)
def states():
    return jsonify({"states": "listes of the states"})