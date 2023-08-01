import os
from sqlalchemy import create_engine

SECRET_KEY = os.urandom(32)

DEBUG = True

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:123456789@localhost/postgres"
SQLALCHEMY_TRACK_MODIFICATIONS = True

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    isolation_level="SERIALIZABLE",
)

engine.connect()