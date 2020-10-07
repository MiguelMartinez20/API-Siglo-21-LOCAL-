from django.contrib import admin
from .models import Cliente, Orden, Mesa, Producto, Receta, Reserva, Movimiento

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Orden)
admin.site.register(Mesa)
admin.site.register(Producto)
admin.site.register(Receta)
admin.site.register(Movimiento)
admin.site.register(Reserva)