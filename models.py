from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from random import randint
# from app import app

db = SQLAlchemy()
migrate = Migrate(db)

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), unique=True, nullable=False)
  email = db.Column(db.String(50), unique=True, nullable=False)
  password = db.Column(db.String(50), unique=True, nullable=False)
  created_at = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

  def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = password

  def to_dict(self):
      return {
        'id':self.id,
        'name':self.name,
        'email':self.email,
        'password':self.password
      }

class Photo(db.Model):
  __tablename__ = 'photos'
  id = db.Column(db.Integer, primary_key=True)
  caption = db.Column(db.String(50), unique=True, nullable=False)
  user_id = db.Comumn(db.Integer, nullable=False)

  def __init__(self, caption, user_id):
    self.caption = caption
    self.user_id = user_id

  def to_dict(self):
    return {
      'id': self.id,
      'caption' : self.caption,
      'user_id' : self.user_id
    }

