import os


class config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'abc123')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
