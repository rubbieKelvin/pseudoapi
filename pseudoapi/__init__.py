import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api


basedir = os.path.abspath(os.path.dirname(__file__))

def createapp(**config):
	app = Flask(__name__)
	app.config.update(config)

	db = SQLAlchemy(app)
	api = Api(app)

	return app, db, api

app, db, api = createapp(
	SQLALCHEMY_DATABASE_URI = "postgres://npwimzpvnqdqim:6f1af506bd28b50fd6d5876bbfe6563cc294d7056879c2ff2e2510444ed487d0@ec2-3-208-50-226.compute-1.amazonaws.com:5432/d5vf5649spjd86",
	SQLALCHEMY_TRACK_MODIFICATIONS = False,
	SECRET_KEY="e\x19\x0c\x97\x14U\xd5#\x89\xf7\x89D\x9f\x1c\xcb\x9e\x9cS\xc2\x8f"
)