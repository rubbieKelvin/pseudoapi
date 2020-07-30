import json
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as lazy_

def validate_json(value):
	try:
		json.loads(value)
	except json.JSONDecodeError as e:
		raise ValidationError(lazy_("%(data) is not a json string"), params=dict(data=value))