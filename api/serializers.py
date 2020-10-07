from rest_framework import serializers
from .models import Cliente, Orden, Mesa, Producto, Receta, Movimiento

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = (
            'id',
            'run',
            'dv',
            'nombre',
            'telefono',
            'email'
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
            'minutos', 
            'recetas',
            'movimiento'
        )

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = (
            'numero',
            'capacidad',
            'disponibilidad'
        )

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = (
            'numero',
            'nombre',
            'costo',
            'stock',
            'embalaje',
            'detalle', 
            'movimiento'
        )

class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = (
            'numero',
            'nombre',
            't_preparacion',
            'precio',
            'grupo',
            'sub_grupo',
            'productos'
        )

class MovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimiento
        fields = (
            'numero',
            'ingreso',
            'egreso',
            'fecha',
            'detalle'
        )