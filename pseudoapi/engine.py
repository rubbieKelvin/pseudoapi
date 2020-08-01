import json
import random
from .models import PseudoAPI

class PseudoEngine:

	def __init__(self, model:PseudoAPI, form:dict, param:dict):
		self.model = model
		self.form  = form.copy()
		self.param = param.copy()

	@property
	def builtinvars(self) -> dict:
		rn10 = random.randint(0, 10)
		rn100 = random.randint(0, 100)
		rn1000 = random.randint(0, 1000)

		def rpw():
			return "************"

		return {
			"$randomNumber10": rn10,
			"$randomNumber100": rn100,
			"$randomNumber1000": rn1000,
			"$randomPassword": rpw()
		}

	def validateform(self):
		modelrequestjson = json.loads(self.model.request)

		# ERRORS THAT COULD OCCUR HERE -.
		# 1. FIELD NOT PROVIDED ERROR
		# 2. INVALID DATATYPE FOR FIELD

		# loop through modelrequest not form
		for key in modelrequestjson:
			formvalue = self.form.get(key)

			if formvalue is None:
				# ERROR 1
				return dict(error=f"field for \"{key}\" not found"), 404

			else:
				# lets assume datatypes in the designs has been validated eg: key="int"
				if type(formvalue) == eval(modelrequestjson[key]):
					pass

				else:
					# ERROR 2
					return dict(
						error=f"invalid datatype for \"{key}\", expected {modelrequestjson[key]}, got {str(type(formvalue))}"
					), 400

	def response(self):
		if self.model.many:
			result = []
			count = int(self.param.get("count", "5"))

			for i in range(count):
				data = self.response_()
				if not data.get("id"):
					data["id"] = i
				result.append(data)

			return result
		return self.response_()

	def response_(self) -> dict:
		validation = self.validateform()

		if type(validation) == tuple:
			return validation

		modelresponsejson = json.loads(self.model.response)

		# THINGS THAT COULD GO WRONG
		result = dict()
		variables = dict()

		variables.update(self.builtinvars)
		variables.update(self.form)

		for key in modelresponsejson:
			value = modelresponsejson[key]

			if type(value) == str:
				value:str	# annotation

				try:
					result[key] = value.format(**variables)
				except KeyError:
					result[key] = value

				continue

			result[key] = value

		return result