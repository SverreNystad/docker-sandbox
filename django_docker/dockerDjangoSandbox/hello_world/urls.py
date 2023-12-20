from django.urls import path
from hello_world.views import index

urlpatterns = [
    path("", index, name="index"),
]