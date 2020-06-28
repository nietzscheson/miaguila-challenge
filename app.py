from flask import Flask, url_for, request
from flask_restful import Resource, Api
from flask_swagger_ui import get_swaggerui_blueprint
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import json
from bson import json_util

app = Flask(__name__)
api = Api(app)

app.config["MONGO_URI"] = "mongodb://root:example@mongo:27017/trips?authSource=admin"

mongo = PyMongo(app)

trips = mongo.db.trips

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

class TripsCreate(Resource):

    def post(self):
    
        data = request.get_json(force=True)

        trip = trips.insert_one(data).inserted_id

        one = trips.find_one({'_id': ObjectId(trip) })

        return {'data': json.dumps(one, default = json_util.default)}

class TripsUpdate(Resource):
    def put(self, id):

        data = request.get_json(force=True)

        id = ObjectId(id)

        trip = trips.find_one_and_update({"_id": id}, {'$set': data})

        return {'data': json.dumps(data, default = json_util.default)}

class TotalTrips(Resource):
    def get(self):

        total = trips.find().count()

        return {'data': total}

class TotalTripsPerCity(Resource):
    def get(self, id):

        total = trips.find({"city": {"name": id}}).count()

        if total == 0:
           return {'data': "Doesn't exists trips for %s" % id }, 204
        return {'data': total}

api.add_resource(TripsCreate, SWAGGER_URL + '/trips')
api.add_resource(TripsUpdate, SWAGGER_URL + '/trips/<id>')
api.add_resource(TotalTrips, SWAGGER_URL + '/trips/total')
api.add_resource(TotalTripsPerCity, SWAGGER_URL + '/trips/cities/<id>')

@app.route('/')
def hello():
    return 'MiAguila Challenge'