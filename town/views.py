from django.shortcuts import render
import pandas as pd
from town.models import Town
from .serializers import TownSerializer
from rest_framework import status , viewsets ,generics 
from rest_framework.response import Response

# Create your views here.
class CreateTown(generics.CreateAPIView):
    querySet=Town.objects.all()
    serializer_class=TownSerializer
class ListTown(viewsets.ViewSet):
    def list(self ,request):
        serializer = TownSerializer(Town.objects.all(), many=True)
        
        df=pd.DataFrame(data=serializer ,orient='columns')
        return Response({
            'data': serializer.data
            
        })
    
class TownViewset(viewsets.ViewSet):
    def update(self ,request , pk=None):
        town=Town.objects.get(id=pk)
        serializer=TownSerializer(instance=town ,data=request.data , partial=True)
        serializer.is_valid(raise_eception=True)
        serializer.save()
        return Response({
            'data':serializer.data
        })
    def delete(self, request ,pk=None):
        town=Town.objects.get(id=pk)
        town.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


