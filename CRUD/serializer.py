from rest_framework import serializers
from .models import Crud

class CrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crud
        fields = '__all__'
        # si tuviera muchos elementos
        # fields ='__all__' Esto me añade todos los campos del modelo