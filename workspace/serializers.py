from . import models
from rest_framework.serializers import ModelSerializer

class FakeAPISerializer(ModelSerializer):
    class Meta:
        model = models.FakeApi
        fields = "__all__"
        read_only_fields = ["id", "route"]
