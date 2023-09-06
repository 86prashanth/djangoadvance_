from django.urls import path 
from musicapp.views import *

urlpatterns = [
    path("", index, name="index"),
]