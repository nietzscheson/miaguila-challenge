from flask import Flask, url_for
from flask_restful import Resource, Api
from flask_swagger_ui import get_swaggerui_blueprint
from flask_pymongo import PyMongo

app = Flask(__name__)
api = Api(app)

app.config["MONGO_URI"] = "mongodb://root:example@mongo:27017/trips?authSource=admin"

mongo = PyMongo(app)

SWAGGER_URL = '/v1'
with app.test_request_context():
    API_URL = url_for('static', filename='swagger.json')
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "MiAguila Challenge"
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

class TotalTrips(Resource):
    def get(self):

        total = mongo.db.trips.find().count()

        return {'total': total}

api.add_resource(TotalTrips, '/trips/total')