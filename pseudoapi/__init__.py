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
	SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(basedir, "pseudoapi.sqlite3"),
	SQLALCHEMY_TRACK_MODIFICATIONS = False,
	SECRET_KEY="e\x19\x0c\x97\x14U\xd5#\x89\xf7\x89D\x9f\x1c\xcb\x9e\x9cS\xc2\x8f"
)