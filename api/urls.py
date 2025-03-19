from django.urls import path
from . import views

urlpatterns = [
    path("shortvideo/create/", views.CreateShortVideo.as_view(), name="short video list"),
    path("shortvideo/delete/<str:pk>/",views.DeleteShortVideo.as_view(), name="delete short video"),
]