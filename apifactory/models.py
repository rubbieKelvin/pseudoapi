import json
from django.db import models
from base64 import urlsafe_b64encode
from django.core.exceptions import ValidationError

from . import validators
from .builtinfuncs import BUILTINS

def type_(data:str):
	if not type(data) == str:
		return type(data)
	
	if data.startswith("::") and " " not in data:
		return eval(data[2:])

def givevar(initstr:str, vardict):
	initstr = initstr.strip()

	if initstr.startswith("$"):
		if initstr in vardict:
			return vardict[initstr]()

	try:
		return initstr.format(**vardict)
	except KeyError as e:
		return None


# Create your models here.
class PseudoApi(models.Model):
	id = models.AutoField(primary_key=True)

	method = models.CharField(max_length=8)
	route  = models.CharField(max_length=255, blank=True)

	body_request  = models.TextField(validators=[validators.validate_json])
	body_response = models.TextField(validators=[validators.validate_json])

	date_created  = models.DateTimeField(auto_now_add=True)


	def makeroute(self):
		self.route = urlsafe_b64encode(bytes(str(self.id), "utf8")).decode("utf8")

	def __str__(self):
		return f"<api route=\"{self.route}\">"


	def typedtemplate(self, pythonjsondata, typefunction=type):
		"makes a typed container or just a type, with the typefunction"

		if type(pythonjsondata) == dict:
			result = dict()

			for key in pythonjsondata:
				result[key] = self.typedtemplate(pythonjsondata[key], typefunction=typefunction)

			return result

		elif type(pythonjsondata) == list:
			result = []

			for i in pythonjsondata:
				result.append(self.typedtemplate(i))

			return result

		return typefunction(pythonjsondata)


	def validaterequest(self, request_data):
		"check if requestbody is equals requestdata"

		request_template = json.loads(self.body_request)

		return (
			self.typedtemplate(request_template, typefunction=type_) \
			== \
			self.typedtemplate(request_data, typefunction=type)
		)


	def lineardict(self, data, container, prefix="%"):
		"makes a linear dictionary from a tree dictionary"
		for key in data:
			if type(data[key]) == dict:
				lineardict(data[key], container, prefix=f"{prefix}{key}.")
			else:
				container[f"{prefix}{key}"] = data[key]

	def feedvars(self, data, vars):
		if type(data) == dict:
			for key in data:
				rslv = self.feedvars(data[key], vars=vars)
				if rslv: data[key] = rslv

		elif type(data) == list:
			for index, value in enumerate(data):
				rslv = self.feedvars(value, vars=vars)
				if rslv: data[index] = self.feedvars(value, vars=vars)

		elif type(data) == str:
			return givevar(data, vars)

		else:
			return data

	def generateresponse(self, request_data, params):
		request_data = request_data.dict()

		if self.validaterequest(request_data):
			resp = json.loads(self.body_response)
			vars = BUILTINS.copy()

			self.lineardict(request_data, vars)
			self.feedvars(resp, vars)

			return resp
		
		return None