from rest_framework import serializers
from .models import Cliente, Orden, Mesa, Producto, Receta, Movimiento, Notificacion, Rol
from django.contrib.auth.models import User

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
            'metodo',
            'detalle'
        )

class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = (
            'numero',
            'estado',
            'fecha',
            'mesa',
            'detalle'
        )

class RolSerializer(serializers.ModelSerializer):

    #usuario = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Rol
        fields = (
            'usuario',
            'rol'
        )

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            'username', 
            'email',
            'first_name', 
            'last_name', 
            'groups'
        )
