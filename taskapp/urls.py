from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from taskapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', note_post, name='note_post' ),
     path('posts/', task_list, name='task_list'),
    path('posts/<int:post_id>', task_view,  name='task_view'), 
 
]