# relevant imports
from flask import Flask, request
from flask_restx import Api, Namespace
from flask_cors import CORS
import os

# defining the app
app = Flask(__name__)
CORS(app)

# defining the app as api and adding other relevant information
api = Api(
    app,
    doc='/doc',
    title="GoCash",
    description="backend doc for GoCash"
)

# logic to pickup stuff from the config file
app.config.from_pyfile(os.path.join("../", "config/app.conf"), silent=False)
