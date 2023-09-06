from django.db import models

class Country(models.Model):
    country_name = models.CharField(null=True, max_length=100)
    country_code = models.IntegerField(null= True)
    country_description = models.CharField(null= True, max_length=200)
    popular_cities = models.CharField(null= True, max_length= 100, unique=True)
    education_rating = models.IntegerField(null=True)
    image_url = models.ImageField(max_length=500)

    def __str__(self):
        return self.country_name