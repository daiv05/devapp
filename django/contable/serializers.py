# import sereliazers from the REST framework
from rest_framework import serializers
  
# import the todo data model
from .models import Cuenta
  
# create a sereliazer class
class CuentaSerializer(serializers.ModelSerializer):
  
    # create a meta class
    class Meta:
        model = Cuenta
        fields = ('idcuenta', 'codigo_cuenta','tipocuenta','nombre_cuenta')