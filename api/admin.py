from django.contrib import admin
from .models import Cliente, Orden, Mesa, Producto, Receta

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Orden)
admin.site.register(Mesa)
admin.site.register(Producto)
admin.site.register(Receta)