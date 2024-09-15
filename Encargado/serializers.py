from rest_framework import serializers
from .models import Encargado

class EncargadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encargado
        fields = '__all__'