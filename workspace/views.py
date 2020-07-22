from django.shortcuts import render
from rest_framework import generics, views, response

from . import models
from . import serializers

# Create your views here.
class FakeAPIView(generics.ListAPIView):
    queryset = models.FakeApi.objects.all()
    serializer_class = serializers.FakeAPISerializer

class FakeAPICreateView(views.APIView):
    def post(self, request):
        print(dir(request))
        return response.Response(dict(msg="hello world"))