from django.urls import path
from Todolist.views import *

urlpatterns = [
    path('', index, name='index'),
    path('delete/<str:pk>',delete,name='delete')
    
]