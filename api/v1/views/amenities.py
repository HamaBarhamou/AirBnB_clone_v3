#!/usr/bin/python3
"""
amenities api
"""


from os import abort
from models import storage
from models.amenity import Amenity
from api.v1.views import app_views
from flask import jsonify, abort, request


@app_views.route('/amenities',
                 strict_slashes=False,
                 methods=['GET'])
def getAmenities():
   am = storage.get(Amenity).values()
   tab = []
   for loop in am:
       tab.append(loop.to_dict())
   return tab, 200