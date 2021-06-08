# from flask_restful import Resource
# class app_route(Resource):
#
#     def get(self):
#         return {'hello': "world"}

from flask import Blueprint, render_template
hello_bp = Blueprint('first_route', __name__, url_prefix='/')

@hello_bp.route("/")
def index():
    return render_template('index.html')

@hello_bp.route("/test")
def index_test():
    return {"id": "test"}