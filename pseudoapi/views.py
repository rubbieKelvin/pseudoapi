from .models import *
from . import app, api
from urllib.parse import unquote

from .engine import PseudoEngine
from flask import request, render_template
from flask_restful import Resource, reqparse

@app.route("/")
def index():
	return render_template("index.html")


class CreateApiView(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument("many", help="return the response as a list of object")
	parser.add_argument("request", 	type=str,  help="json string representing <key=type> object")
	parser.add_argument("response", type=str,  help="json string representing how data should be returned")
	parser.add_argument("method", 	type=str,  help="http method for this fake api")


	def post(self):
		"""create a new fake api"""
		data = CreateApiView.parser.parse_args()

		many = True if data.get("many")=="True" else False 

		newapi = PseudoAPI(
			many=many, 
			request=data.get("request"), 
			response=data.get("response"), 
			method=data.get("method")
		)
		db.session.add(newapi)
		db.session.commit()

		newapi.makeroute()
		db.session.add(newapi)
		db.session.commit()

		return newapi.dictionary()


class CallApiView(Resource):

	def all(self, route, method):
		route = unquote(route)
		api = PseudoAPI.query.filter_by(route=route).first_or_404()


		if not api.method == method:
			return {"error":"method not supported"}, 405

		engine = PseudoEngine(api, form=request.form, param=request.args)

		return engine.response()

	def get(self, route):
		return self.all(route, "get")

	def post(self, route):
		return self.all(route, "post")


api.add_resource(CreateApiView, "/workspace/apis/")
api.add_resource(CallApiView, "/<route>")