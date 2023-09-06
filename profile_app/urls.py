from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home-page'),
    path('profile/', UserProfile.as_view(), name='user-profile' ),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]