from django.shortcuts import render
from django.views import View
from .models import Skills, Location
from django.core import serializers

class AutocompleteSearchFilter(View):
    def get(self, request):
        skills = Skills.objects.all()
        locations = Location.objects.all()
        skills_list = serializers.serialize('json',list(skills))
        location_list = serializers.serialize('json',list(locations))
        context = {'skills':skills_list, 'locations':location_list}
        return render(request, 'search_filter/index.html', context)