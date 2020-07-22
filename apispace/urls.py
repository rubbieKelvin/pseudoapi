from django.urls import path

from . import views

urlpatterns = [
    path("dev/", views.DevView.as_view(), name="dev-list-create"),
    path("dev/<int:pk>", views.DevDetailView.as_view(), name="dev-getdetails-delete"),
    path("dev/token", views.DevByToken.as_view(), name="dev-by-token")
]