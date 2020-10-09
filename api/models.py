from django.db import models
from django.utils import timezone

# Create your models here.

class Cliente(models.Model):
    id = models.AutoField(primary_key= True)
    run =  models.CharField(max_length = 8)
    dv = models.CharField(max_length = 1, default='0')
    nombre = models.CharField(max_length = 255)
    telefono = models.CharField(max_length = 12)
    email = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.nombre

class Mesa(models.Model):

    OCUPADA = 'OCUPADA'
    RESERVADA = 'RESERVADA'
    DISPONIBLE = 'DISPONIBLE'
    

    STATE_CHOICES = (
        (OCUPADA, 'OCUPADA'),
        (RESERVADA, 'RESERVADA'),
        (DISPONIBLE,'DISPONIBLE'),
    )
    
    numero = models.IntegerField(primary_key= True)
    capacidad = models.IntegerField(blank=True)
    disponibilidad =  models.CharField(max_length=11, choices=STATE_CHOICES, default=DISPONIBLE)

    def __str__(self):
        return str(self.numero)

class Movimiento(models.Model):

    numero = models.AutoField(primary_key= True)
    ingreso = models.IntegerField(default=0)
    egreso = models.IntegerField(default=0)
    fecha = models.DateTimeField(default=timezone.now, blank=True)
    detalle = models.CharField(max_length = 255)

    def __str__(self):
        return str(self.numero)

class Producto(models.Model):

    GRANEL = 'GRANEL'
    ENVASADO = 'ENVASADO'

    STATE_CHOICES = (
        (GRANEL, 'GRANEL'),
        (ENVASADO, 'ENVASADO'),
    )

    numero = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length = 255)
    costo = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    embalaje = models.CharField(max_length=11, choices=STATE_CHOICES, default=GRANEL)
    detalle = models.CharField(max_length = 300, blank=True)
    movimiento = models.OneToOneField(Movimiento, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Receta(models.Model):

    ENTRADA = 'ENTRADA'
    PLATO_FONDO = 'PLATO_FONDO'
    APERITIVO = 'APERITIVO'
    AGREGADO = 'AGREGADO'
    BEBESTIBLE = 'BEBESTIBLE'
    BAJATIVO = 'BAJATIVO'
    POSTRE = 'POSTRE'

    SOPAS = 'SOPAS'
    CREMAS = 'CREMAS'
    CARNES_ROJAS = 'CARNES_ROJAS'
    CARNES_BLANCAS = 'CARNES_BLANCAS'
    PESCADOS = 'PESCADOS'
    MARISCOS = 'MARISCOS'
    CALDOS = 'CALDOS'
    LEGUMBRES = 'LEGUMBRES'
    PASTELES = 'PASTELES'
    EMBUTIDOS = 'EMBUTIDOS'
    EMPANADAS = 'EMPANADAS'
    ENSALADAS = 'ENSALADAS'
    VINOS = 'VINOS'
    BEBIDAS = 'BEBIDAS'
    JUGOS = 'JUGOS'
    HELADOS = 'HELADOS'
    TORTAS = 'TORTAS'
    KUCHENS = 'KUCHENS'
    OTRO = 'OTRO'

    STATE_CHOICES1 = (
        (ENTRADA, 'ENTRADA'),
        (PLATO_FONDO, 'PLATO_FONDO'),
        (APERITIVO, 'APERITIVO'),
        (AGREGADO, 'AGREGADO'),
        (BEBESTIBLE, 'BEBESTIBLE'),
        (POSTRE, 'POSTRE'),
    )

    STATE_CHOICES2 = (
        (SOPAS, 'SOPAS'),
        (CREMAS, 'CREMAS'),
        (CARNES_ROJAS, 'CARNES_ROJAS'),
        (CARNES_BLANCAS, 'CARNES_BLANCAS'),
        (PESCADOS, 'PESCADOS'),
        (MARISCOS, 'MARISCOS'),
        (CALDOS, 'CALDOS'),
        (LEGUMBRES, 'LEGUMBRES'),
        (PASTELES, 'PASTELES'),
        (EMBUTIDOS, 'EMBUTIDOS'),
        (EMPANADAS, 'EMPANADAS'),
        (VINOS, 'VINOS'),
        (BEBIDAS, 'BEBIDAS'),
        (JUGOS, 'JUGOS'),
        (BAJATIVO, 'BAJATIVO'),
        (HELADOS, 'HELADOS'),
        (TORTAS, 'TORTAS'),
        (KUCHENS, 'KUCHENS'),
        (OTRO, 'OTRO'),
    )

    numero = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length = 255)
    t_preparacion = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)
    grupo = models.CharField(max_length=20, choices=STATE_CHOICES1, default=ENTRADA)
    sub_grupo = models.CharField(max_length=20, choices=STATE_CHOICES2)
    productos = models.ManyToManyField(Producto)

    def __str__(self):
        return self.nombre

class Reserva (models.Model):

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False, blank=False)
    mesa_num = models.ForeignKey(Mesa, on_delete=models.CASCADE, null=False, blank=False)
    fecha = models.DateField()
    hora = models.TimeField() 
    observacion = models.CharField(max_length = 255, blank=True)

    def __str__(self):
        return str(self.id)

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
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, blank=False, null=False)
    recetas = models.ManyToManyField(Receta)
    movimiento = models.OneToOneField(Movimiento, on_delete=models.CASCADE, blank=True, null=True)

    def publish(self):
        self.hora_ter = timezone.now()
        self.save()

    def __str__(self):
        return str(self.numero)