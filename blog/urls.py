from django.urls import path
from blog.views import *

urlpatterns = [
    path('create/', create_post, name = "create_post")
]