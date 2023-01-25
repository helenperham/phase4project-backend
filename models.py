from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from random import randint
# from app import app

db = SQLAlchemy()
migrate = Migrate(db)
