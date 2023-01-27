import os
from flask import Flask, send_file, request, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
import config

from models import db, User

app = Flask(__name__, static_folder='public')
CORS(app, origins=['*'])
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.sqlite3'
db.init_app(app)
migrate = Migrate(app, db)

# @app.route("/")
# def hello():
#     return "Hello, World!"
# # @app.get('./ this is the routes to different components')


@app.get('/users')
def all_staff():
    user = User.query.all()
    return jsonify([s.to_dict() for s in user]), 201


@app.get('/profile')
def profile():
    staff = User.query.all()
    return jsonify([s.to_dict() for s in profile]), 201


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=os.environ.get('PORT', 3000))
