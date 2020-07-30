from django.urls import path
from .views import PsuedoApiListCreateView, call_pseudoapi

urlpatterns = [
	path("apis/", PsuedoApiListCreateView.as_view(), name="create apis"),
	path("api/<str:route>/", call_pseudoapi, name="call api")

]