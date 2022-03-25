from dataclasses import fields
from pyexpat import model
from .models import  Town 
from rest_framework import serializers

class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model=Town
        fields=('id' ,'code' , 'name' , 'population' ,'average_age' ,'district_code' ,'departement_code' ,'region_code' ,'region_name')
