from django.shortcuts import render
from rest_framework import generics, views, response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_409_CONFLICT
from rest_framework.renderers import JSONRenderer

from . import models
from . import serializers

def ensure(dictionary:dict, keys:list) -> str:
    for key in keys:
        if dictionary.get(key) is None:
            return key
    return ""

# Create your views here.
class FakeAPIView(generics.ListAPIView):
    queryset = models.FakeApi.objects.all()
    serializer_class = serializers.FakeAPISerializer

class FakeAPICreateView(views.APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        required = ["name",]
        req = ensure(request.data, required)

        if not req:
            fakeapi = models.FakeApi(user=request.user, name=request.data.get("name"), descr=request.data.get("descr", ""))
            fakeapi.save()

            fakeapisr = serializers.FakeAPISerializer(fakeapi)
            return response.Response(fakeapisr.data)
        return response.Response(dict(error="name field is required"), status=HTTP_409_CONFLICT)
