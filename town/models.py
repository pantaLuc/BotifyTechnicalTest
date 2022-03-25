from django.db import models

# Create your models here.
class Town(models.Model):
    code=models.IntegerField()
    name=models.CharField(max_length=100)
    population=models.IntegerField()
    average_age=models.FloatField()
    district_code=models.IntegerField()
    departement_code=models.CharField(max_length=20)
    region_code=models.IntegerField()
    region_name=models.CharField(max_length=200)