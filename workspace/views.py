from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework import generics, views, response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from rest_framework.status import HTTP_409_CONFLICT
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_405_METHOD_NOT_ALLOWED

import json
import logging
from . import models
from . import serializers
from .pseudoapifactory import processresponse

def ensure(dictionary:dict, keys:list) -> str:
    for key in keys:
        if dictionary.get(key) is None:
            return key
    return ""

def makedict(data) -> dict:
    if type(data) == dict:
        return data
    elif type(data) == str:
        return json.loads(data)
    else:
        logging.error(f"invalid type {type(data)}")
        raise Exception(f"invalid type {type(data)}")

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
            request_body = makedict(request.data.get("body_request", {}))
            response_body = makedict(request.data.get("body_response", {}))

            fakeapi = models.FakeApi(
                user=request.user,
                name=request.data.get("name"),
                descr=request.data.get("descr", ""),
                method=request.data.get("method", "GET"),
                body_response=response_body,
                body_request=request_body
            )
            fakeapi.save()

            fakeapi.generateRoute()

            fakeapisr = serializers.FakeAPISerializer(fakeapi)
            return response.Response(fakeapisr.data)
        return response.Response(dict(error="name field is required"), status=HTTP_409_CONFLICT)

class FakeApiRouterView(views.APIView):
    def processrequest(self, method, request, id, name):
        fakeapi = models.FakeApi.objects.filter(id=id, name=name).first()

        if fakeapi:

            if fakeapi.method.lower() != method:
                return response.Response(dict(error="Method not allowed."), status=HTTP_405_METHOD_NOT_ALLOWED)

            return response.Response(
                processresponse(
                    request.data,
                    fakeapi.body_request,
                    fakeapi.body_response
                ),
                status=HTTP_200_OK
            )
            
        return response.Response(dict(error="this route was not found"), status=HTTP_404_NOT_FOUND)


    def get(self, request, id, name):
        # get api for this request
        return self.processrequest("get", request, id, name)

    def post(self, request, id, name):
        # post api for this request
        return self.processrequest("post", request, id, name)


    def put(self, request, id, name):
        return response.Response(dict(message="api routes for the method is still under construction"))

    def delete(self, request, id, name):
        return response.Response(dict(message="api routes for the method is still under construction"))
        