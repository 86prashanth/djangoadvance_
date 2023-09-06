from django.urls import path
from autocomplete_search_filter.views import AutocompleteSearchFilter

urlpatterns = [
    path('', AutocompleteSearchFilter.as_view(), name= 'search-filter')
]