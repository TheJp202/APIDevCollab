from rest_framework import serializers
from .models import ClienteEspacio

class ClienteEspacioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteEspacio
        fields = '__all__'