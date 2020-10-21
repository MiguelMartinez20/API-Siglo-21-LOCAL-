from django.shortcuts import render

# Create your urls here.

from django.urls import path
from .views import ClienteList, OrdenList, OrdenUpdate, OrdenDetail, MesaList, MesaDetail, MesaUpdate, ProductoList, ProductoDetail, ProductoUpdate, RecetaList, RecetaDetail, RecetaUpdate, Logout, MovimientoList, MovimientoDetail, MovimientoUpdate, NotificacionList, NotificacionDetail, NotificacionUpdate

urlpatterns = [
    path('cliente/', ClienteList.as_view(), name='cliente_list'),
    path('orden/', OrdenList.as_view(), name='orden_list'),
    path('orden/<int:numero>/', OrdenDetail.as_view(), name='orden_detail'),
    path('orden/<int:numero>/editar_orden/', OrdenUpdate.as_view(), name='orden_update'),
    path('mesa/', MesaList.as_view(), name='mesa_list'),
    path('mesa/<int:numero>/', MesaDetail.as_view(), name='mesa_detail'),
    path('mesa/<int:numero>/editar_mesa/', MesaUpdate.as_view(), name='mesa_update'),
    path('producto/', ProductoList.as_view(), name='producto_list'),
    path('producto/<int:numero>/', ProductoDetail.as_view(), name='producto_detail'),
    path('producto/<int:numero>/editar_producto/', ProductoUpdate.as_view(), name='producto_update'),
    path('receta/', RecetaList.as_view(), name='receta_list'),
    path('receta/<int:numero>/', RecetaDetail.as_view(), name='receta_detail'),
    path('receta/<int:numero>/editar_receta/', RecetaUpdate.as_view(), name='receta_update'),
    path('movimiento/', MovimientoList.as_view(), name='movimiento_list'),
    path('movimiento/<int:numero>/', MovimientoDetail.as_view(), name='movimiento_detail'),
    path('movimiento/<int:numero>/editar_movimiento/', MovimientoUpdate.as_view(), name='movimiento_update'),
    path('notificacion/', NotificacionList.as_view(), name='notificacion_list'),
    path('notificacion/<int:numero>/', NotificacionDetail.as_view(), name='notificacion_detail'),
    path('notificacion/<int:numero>/editar_notificacion/', NotificacionUpdate.as_view(), name='notificacion_update'),
    path('logout/', Logout.as_view(), name='logout'),
]
