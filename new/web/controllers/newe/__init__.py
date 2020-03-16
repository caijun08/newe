from flask import Blueprint, render_template, request,jsonify
from common.libs.Helper import Helper
from common.libs.Spider import Spider
from application import app
route_newe = Blueprint('route_newe', __name__)

from . import newe
