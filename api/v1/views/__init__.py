#!/usr/bin/python3
"""
Initializes views module
"""

from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
app_views_state = Blueprint('app_views_state', __name__, url_prefix='/api/v1')
from api.v1.views.index import *
