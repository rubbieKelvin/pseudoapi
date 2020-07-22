from django.shortcuts import render

# Create your views here.
from .models import Dev
from .serializers import DevSerializer
from rest_framework import generics, views

class DevByTokenView(views.APIView):
    def post(self, request):
        return ""

class DevView(generics.ListCreateAPIView):
    """
    get: gets dev list
    post: creates dev
    """
    queryset = Dev.objects.all()
    serializer_class = DevSerializer
    
class DevDetailView(generics.RetrieveDestroyAPIView):
    """
    """
    queryset = Dev.objects.all()
    serializer_class = DevSerializer