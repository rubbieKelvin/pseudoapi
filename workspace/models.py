from django.db import models
from django.contrib.auth.models import User

from . import fields
from .builtinvars import BuiltinVars

builtinvars = BuiltinVars()

# Create your models here.
class FakeApi(models.Model):
    METHODS = "post, get, delete, put, patch, copy, head, option"
    METHODS = list(
        map(
            lambda method: (method.strip(), method.upper().strip()),
            METHODS.split(",")
        )
    )
    id      = models.AutoField(primary_key=True)
    user    = models.ForeignKey(User, on_delete=models.CASCADE, related_name="apis")
    name    = models.CharField(max_length=15)
    descr   = models.TextField(null=True, blank=True)
    method  = models.CharField(max_length=10, choices=METHODS)
    route   = models.CharField(max_length=255, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    body_request = fields.JsonField()
    body_response= fields.JsonField()

    def generateRoute(self):
        self.route = f"{self.id}/{self.name}"
        self.save()

    def __str__(self):
        return f"<api route=\"{self.route}\">"

    def __repr__(self):
        return str(self)