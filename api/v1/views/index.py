#!/usr/bin/python3
"""Retrieves number for each type"""

from api.v1.views import app_views, app_views_state
from flask import jsonify
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    return jsonify({"status": "OK"})


@app_views_state.route('/stats', strict_slashes=False)
def stats():
    return jsonify(
        {
            "amenities": storage.count(Amenity),
            "cities": storage.count(City),
            "places": storage.count(Place),
            "reviews": storage.count(Review),
            "states": storage.count(State),
            "users": storage.count(User)
        }
    )
