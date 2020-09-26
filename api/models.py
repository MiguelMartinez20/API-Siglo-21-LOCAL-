from django.db import models
from django.utils import timezone

# Create your models here.
        
class Orden(models.Model):
    
    ENTREGADA = 'ENTREGADA'
    LISTA = 'LISTA'
    PREPARACION = 'PREPARACION'
    

    STATE_CHOICES = (
        (ENTREGADA, 'ENTREGADA'),
        (LISTA, 'LISTA'),
        (PREPARACION, 'PREPARACION'),
    )

    numero = models.AutoField(primary_key= True)
    estado =  models.CharField(max_length=11, choices=STATE_CHOICES, default=PREPARACION)
    hora_ini = models.DateTimeField(default=timezone.now, blank=True)
    hora_ter = models.DateTimeField(blank=True, null=True)
    detalle = models.CharField(max_length=255, blank=True)
    total = models.IntegerField(blank=True)
    minutos = models.IntegerField(default=5, blank=True) 
    mesa = models.IntegerField(blank=True)

    def publish(self):
        self.hora_ter = timezone.now()
        self.save()

    def __str__(self):
        return str(self.numero)

class Cliente(models.Model):
    id = models.AutoField(primary_key= True)
    run =  models.CharField(max_length = 8)
    dv = models.CharField(max_length = 1, default='0')
    nombre = models.CharField(max_length = 255)
    telefono = models.CharField(max_length = 12)
    email = models.CharField(max_length = 255)
    reserva = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.nombre
