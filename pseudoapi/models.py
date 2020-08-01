from . import db
from datetime import datetime
from base64 import urlsafe_b64encode

class PseudoAPI(db.Model):
	__tablename__ = "pseudoapis"

	route	= db.Column(db.Text, nullable=True)
	id 		= db.Column(db.Integer, primary_key=True)
	created	= db.Column(db.DateTime, default=datetime.now)
	many	= db.Column(db.Boolean, nullable=False)
	request	= db.Column(db.Text, nullable=False, unique=False)
	response= db.Column(db.Text, nullable=False, unique=False)
	method	= db.Column(db.String(10), unique=False, default="get")

	def makeroute(self):
		self.route = urlsafe_b64encode(bytes(str(self.id), "utf8")).decode("utf8")

	def __str__(self):
		return f"<api route=\"{self.route}\">"

	def dictionary(self):
		return dict(
			id=self.id,
			route=self.route,
			many=self.many,
			created=str(self.created),
			request=self.request,
			response=self.response,
			method=self.method
		)