import os
from flask import Flask, send_file, request, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
import config

from models import db

app = Flask(__name__, static_folder='public')
CORS(app, origins=['*'])
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.sqlite3'

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def hello():
    return "Hello, World!"
# @app.get('./ this is the routes to different components')
