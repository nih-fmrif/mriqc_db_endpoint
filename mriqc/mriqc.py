import json
from flask import Flask, jsonify, request, abort
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
from collections import OrderedDict
from functools import wraps

## PyMongo may require a system dependency on CentOS 7
# sudo dnf install python2-pymongo-gridfs

# Instantiate application
app = Flask(__name__)
app.config['MONGO_DBNAME'] = "mriqc"
api = Api(app)
mongo = PyMongo(app)

# Auth Token: change this to something more random
API_KEY = 'ZUsBaabr6PEbav5DKAHIODEnwpwC58oQTJF7KWvDBPUmBIVFFtwOd7lQBdz9r9ulJTR1BtxBDqDuY0owxK6LbLB1u1b64ZkIMd46'


def api_token_required(func):
    """Decorator used to wrap any function requiring the auth token."""
    @wraps(func)
    def decorated(*args, **kwargs):
        if request.headers.get('Token') == API_KEY:
            return func(*args, **kwargs)
        else:
            abort(401)
    return decorated


class Measurement(Resource):
    def get(self, objectid):
        """
        GET method to retrieve single record matching the objectID from the
        database.
        """
        return jsonify(
            mongo.db.measurements.find_one({}, {"_id": objectid})
        )


class Measurements(Resource):
    def get(self):
        """GET method to retrieve all records from the database."""
        return jsonify(
            list(mongo.db.measurements.find({}, {"_id": False}))
        )


class Upload(Resource):
    """
    Upload class for the PUT method to add records.
    Requires decorator to enforce API tokens.
    """
    # Use the api_token_required decorator for uploading records
    method_decorators = [api_token_required]

    def put(self):
        """PUT method to upload a record into the database."""
        if not request.json:
            abort(400)

        metric = OrderedDict(sorted(request.json.items(), key=lambda t: t[0]))

        try:
            rc = mongo.db.measurements.update(metric, metric, upsert=True)
        except:
            raise
        else:
            # Return 201 Created
            return '{"success": "OK"}', 201


# Resource endpoints
api.add_resource(Measurements, '/measurements')
api.add_resource(Measurement, '/measurements/<int:objectid>')
api.add_resource(Upload, '/measurements/upload')


# Main
if __name__ == '__main__':
    host = "0.0.0.0"
    port = 5000

    # Set debug to False for production
    debug = False
    app.run(
        host=host,
        port=port,
        debug=debug
    )
