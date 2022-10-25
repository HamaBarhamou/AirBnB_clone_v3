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
   am = storage.all(Amenity).values()
   tab = []
   for loop in am:
       tab.append(loop.to_dict())
   return tab, 200


@app_views.route('/amenities',
                 strict_slashes=False,
                 methods=['POST'])
def creat_Amenities():
    data = request.get_json()

    if type(data) is not dict:
        abort(404, "Not a JSON")
    if "name" not in data:
        abort(400, "Missing name")
    am = Amenity(**data)
    storage.new(am)
    storage.save()
    return jsonify(am.to_dict()), 201


@app_views.route('/amenities/<amenity_id>',
                 strict_slashes=False,
                 methods=['GET'])
def getAmenities_By_Id(amenity_id):
    am = storage.get(Amenity, amenity_id)
    if am is None:
        abort(404)
    return jsonify(am.to_dict()), 200


@app_views.route('/amenities/<amenity_id>',
                 strict_slashes=False,
                 methods=['DELETE'])
def delAmeneities(amenity_id):
    am = storage.get(Amenity, amenity_id)
    if am is None:
        abort(404)
    storage.delete(am)
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities/<amenity_id>',
                 strict_slashes=False,
                 methods=['PUT'])
def update_Amenitie(amenity_id):
    print("hello update")
    data = request.get_json()

    if type(data) is not dict:
        abort(404, "Not a JSON")
    if "name" not in data:
        abort(400, "Missing name")

    am = storage.get(Amenity, amenity_id)
    if am is None:
        abort(404)
    black_list = ["id", "created_at", "updated_at"]
    for key, value in data.items():
        if key not in black_list:
            setattr(am, key, value)
    storage.save()
    return jsonify(am.to_dict()), 200