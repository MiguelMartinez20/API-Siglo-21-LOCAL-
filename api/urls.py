from django.shortcuts import render

# Create your views here.

from django.urls import path
from .views import ClienteList, OrdenList, OrdenUpdate, OrdenDetail, MesaList, MesaDetail, MesaUpdate, Logout

urlpatterns = [
    path('cliente/', ClienteList.as_view(), name='cliente_list'),
    path('orden/', OrdenList.as_view(), name='orden_list'),
    path('orden/<int:numero>/', OrdenDetail.as_view(), name='orden_detail'),
    path('orden/<int:numero>/editar_orden/', OrdenUpdate.as_view(), name='orden_update'),
    path('mesa/', MesaList.as_view(), name='mesa_list'),
    path('mesa/<int:numero>/', MesaDetail.as_view(), name='mesa_detail'),
    path('mesa/<int:numero>/editar_mesa/', MesaUpdate.as_view(), name='mesa_update'),
    path('logout/', Logout.as_view(), name='logout'),
]
