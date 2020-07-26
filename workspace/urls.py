from django.urls import path
from . import views

urlpatterns = [
    path("all/", views.FakeAPIView.as_view(), name="list-fakeapis"),
    path("new/", views.FakeAPICreateView.as_view(), name="create-fakeapi"),
    path("<int:id>/<str:name>/", views.FakeApiRouterView.as_view(), name="api server")
]