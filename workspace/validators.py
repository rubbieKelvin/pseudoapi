import json
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as lazy

class JsonValidator:
    def __init__(self):
        pass

    def validate(self, value):
        try:
            json.loads(value)
        except json.JSONDecodeError:
            raise ValidationError(lazy("%(value)s is not a json string"), params=dict(
                value=value
            ))