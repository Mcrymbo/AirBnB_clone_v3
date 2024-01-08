#!/usr/bin/python3
""" creating an app file for defining end points """
from flask import Flask, make_response, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import environ
from flasgger import Swagger
from flasgger.utils import swag_from


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

app.config['SWAGGER'] = {
    'title': 'AirBnB clone Restful API',
    'uiversion': 4
}

Swagger(app)



@app.teardown_appcontext
def teardown_session(exception):
    """ closing down the storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ handles 404 error """

    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == '__main__':
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
