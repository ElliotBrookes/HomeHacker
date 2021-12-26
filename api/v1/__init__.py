from . import views, errors
from flask import Blueprint
from flask_restful import Api

v1 = Blueprint('v1', __name__)
api = Api(v1)


api.add_resource(views.HelloWorld, '/')
