from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

def index(request):
    return render(request, "index.html")

@permission_classes([IsAuthenticated])
def home(request):
	return render(request, "home.html")