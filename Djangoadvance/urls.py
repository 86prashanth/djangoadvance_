"""
URL configuration for Djangoadvance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from autocomplete_search_filter.urls import *
from django.conf.urls.static import static
from dictionary.urls import *

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include('accounts.urls')),
    path('profile/', include('profile_app.urls')),
    path('chipfilter/', include('app_chipfilter.urls')),
    path('filter/',include('autocomplete_search_filter.urls')),
    path('blog/',include('blog.urls')),
    path('dictionary/',include('dictionary.urls')),
    path('music/', include('musicapp.urls')),
    path('todolist/', include('Todolist.urls')),
    path('htmleditor/', include('HtmlEditor.urls')),
    path('task/', include('taskapp.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('invoice/', include('pdfinvoice.urls')),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)