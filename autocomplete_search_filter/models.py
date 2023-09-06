from django.db import models

class Skills(models.Model):
    skill_name = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.skill_name

class Location(models.Model):
    location = models.CharField(null= True, max_length=100)

    def __str__(self):
        return self.location