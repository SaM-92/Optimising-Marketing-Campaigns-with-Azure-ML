from flask import Flask, request
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from flask import Flask, request
from werkzeug.utils import secure_filename
import os
import uuid
import pandas as pd
import re
import datetime

# from sub.cal_metrics import *
# from utilities.outputFiles import *
# from utilities.blob_storage import *

# First the Flask class is imported.
# Next an instance of this class is created.
# The first argument is the name of the application’s module or package.
# __name__ is a convenient shortcut for this that is appropriate for most cases.
# This is needed so that Flask knows where to look for resources such as templates and static files.
app = Flask(__name__)
api = Api(app)

# The lines below are used to specify the upload folder either locally or on the Azure server

# deployment Azure
# app.config['UPLOAD_FOLDER'] = '/home/site/wwwroot/uploads/'

# deployment on localhost
app.config["UPLOAD_FOLDER"] = "uploads"


## swagger specific ###

# Swagger page address
SWAGGER_URL = "/swagger"

from flask import send_from_directory


@app.route("/swagger.json")
def send_swagger():
    return send_from_directory(
        "C:\\Users\\saeed.misaghian\\Documents\\Training\\Udacity_ML_Engineering\\MLOps\\nd00333_AZMLND_C2\\starter_files\\swagger",
        "swagger.json",
    )


# Swagger document relative path
API_URL = "/swagger.json"
# API_URL = "C:\\Users\\saeed.misaghian\\Documents\\Training\\Udacity_ML_Engineering\\MLOps\\nd00333_AZMLND_C2\\Exercise_starter_files\\Swagger\\swagger.yaml"


SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Bank Marketing Service API"}
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
## end swagger specific ###


from http.server import HTTPServer, SimpleHTTPRequestHandler, test

import sys


class CORSRequestHandler(SimpleHTTPRequestHandler):
    """
    Allows a simple HTTP server to have CORS enabled by default
    """

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        SimpleHTTPRequestHandler.end_headers(self)


# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         # Allows the port to be passed in as an argument
#         port = sys.argv[-1]
#     else:
#         port = 8000

#     test(CORSRequestHandler, HTTPServer, port=port)

if __name__ == "__main__":
    app.run(debug=True)
