from django.urls import path
from .views import CountryFilter ,ChipFilter

urlpatterns = [
    path('',CountryFilter.as_view(), name='country-filter'),
    path('chipfilter/<str:name>/',ChipFilter.as_view(), name = 'chip-filter')
]