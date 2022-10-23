#!/usr/bin/python3
"""
states api
"""


from models import storage
from models.city import City
from api.v1.views import app_views
from flask import jsonify, request, redirect
from werkzeug.exceptions import HTTPException


@app_views.route('/states/<state_id>/cities',
                 strict_slashes=False,
                 methods=['GET', 'DELETE', 'POST'])
@app_views.route('/cities/<city_id>',
                 strict_slashes=False,
                 methods=['GET', 'DELETE', 'PUT'])
def Cities(state_id=None, city_id=None):
    if request.method == 'GET':
        return jsonify({"msg": "Cities List all"}), 200
