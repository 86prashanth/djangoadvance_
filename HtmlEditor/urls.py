from django.contrib import admin
from django.urls import path,include
from HtmlEditor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('send/',views.sendanemail,name='email'),
]