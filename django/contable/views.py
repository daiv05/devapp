from django.shortcuts import render
  
# import view sets from the REST framework
from rest_framework import viewsets
  
# import the CuentaSerializer from the serializer file
from .serializers import CuentaSerializer
  
# import the Todo model from the models file
from .models import Cuenta
  
# create a class for the Todo model viewsets
class CuentaView(viewsets.ModelViewSet):
  
    # create a sereializer class and 
    # assign it to the TodoSerializer class
    serializer_class = CuentaSerializer
  
    # define a variable and populate it 
    # with the Todo list objects
    queryset = Cuenta.objects.all()