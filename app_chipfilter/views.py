from django.shortcuts import render
from django.views import View
from .models import Country
from django.core import serializers

class CountryFilter(View):
    def get(self, request):
        countries = Country.objects.all()
        countries_list = serializers.serialize('json', list(countries))
        context = {'countries': countries_list}
        return render(request,'chipfilter/index.html',context)
    
class ChipFilter(View):
    def get(sefl, request, name):
        countries = Country.objects.all()
        countries_list = serializers.serialize('json', list(countries))
        countryData = Country.objects.filter(country_name = name)
        country_list = serializers.serialize('json', list(countryData))
        context = {'countries': country_list,'countries_list': countries_list}
        return render(request,'chipfilter/card-list.html',context)