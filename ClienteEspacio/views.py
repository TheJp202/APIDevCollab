from django.shortcuts import render
from .models import ClienteEspacio
from .serializers import ClienteEspacioSerializer
from rest_framework import generics
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#from clienteespacios.signals import clienteespacio_ejecutado, clienteespacio_eliminado

class ClienteEspaciosLCAPIView(generics.ListCreateAPIView):
    queryset = ClienteEspacio.objects.all()
    serializer_class = ClienteEspacioSerializer
    def perform_create(self, serializer):
        clienteespacio = serializer.save()
        #clienteespacio_ejecutado.send(sender=clienteespacios, clienteespacio_id=clienteespacio.id)

class ClienteEspaciosRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClienteEspacio.objects.all()
    serializer_class = ClienteEspacioSerializer
    def perform_update(self, serializer):
        clienteespacio = serializer.save()
        #clienteespacio_ejecutado.send(sender=clienteespacios, clienteespacio_id=clienteespacio.id)

    def perform_destroy(self, instance):
        clienteespacio_id = instance.id
        #clienteespacio_eliminado.send(sender=clienteespacios, clienteespacio_id=clienteespacio_id)
        instance.delete()
        

class CalcularCobroClienteAPIView(APIView):
    
    def get(self, request, pk, *args, **kwargs):
        try:
            cliente_espacio = ClienteEspacio.objects.select_related('Espacio').get(id=pk)
        except ClienteEspacio.DoesNotExist:
            return Response({"error": "ClienteEspacio no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        hora_final = cliente_espacio.HoraFinal or timezone.now()  # Usa HoraFinal si existe, sino la hora actual
        horas_transcurridas = (hora_final - cliente_espacio.HoraInicio).total_seconds() / 3600  # Diferencia en horas
        if horas_transcurridas < 0:
            horas_transcurridas = 0
        costo_horas = round(horas_transcurridas * cliente_espacio.Espacio.CostoHora, 1)  # Calcular el costo total
        costo_reserva_hora = cliente_espacio.Espacio.CostoReservaHora if cliente_espacio.HoraReserva else cliente_espacio.Espacio.CostoHora
        if cliente_espacio.HoraReserva:
            horas_reserva = (cliente_espacio.HoraInicio - cliente_espacio.HoraReserva).total_seconds() / 3600
            cobro_total_reserva = round(costo_horas + (horas_reserva * costo_reserva_hora), 1)
        else:
            cobro_total_reserva = round(costo_horas, 1)
        cobro = {
            'Cliente': cliente_espacio.Cliente.Dni,
            'Espacio': cliente_espacio.Espacio.Numero,  # Asumiendo que el modelo Espacio tiene el atributo Nombre
            'Horas': round(horas_transcurridas, 1),
            'CostoHora': cliente_espacio.Espacio.CostoHora,
            'CobroTotal': costo_horas,
            'CobroTotalReserva': cobro_total_reserva

        }

        return Response(cobro)
    
    
