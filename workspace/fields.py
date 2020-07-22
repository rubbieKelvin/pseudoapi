from . import validators
from json import loads, dumps
from django.db import models


class JsonField(models.TextField):
    def __init__(self, *args, formatter=dict(), **kwargs):
        super(JsonField, self).__init__(*args, **kwargs)
        self.default = dict()

    def to_python(self, value):
        validators.JsonValidator().validate(value)
        return loads(value)

    def from_db_value(self, value, expression, connection):
        return loads(value)


    def get_prep_value(self, value):
        return dumps(value, indent=2)