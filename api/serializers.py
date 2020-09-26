from rest_framework import serializers
from .models import Cliente, Orden

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = (
            'run',
            'nombre',
            'telefono',
            'email',
            'reserva',
        )

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = (
            'numero',
            'estado',
            'hora_ini',
            'hora_ter',
            'detalle',
            'total',
            'mesa',
            'minutos'
        )