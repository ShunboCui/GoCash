from appApi.utils import app
from flask import Flask 
from appApi.routes.routes import *

if __name__ == "__main__":
    app.run(debug=True)