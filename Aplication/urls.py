from django.urls import path
from django.contrib import admin
from Aplication.views import headsets, mouses, teclados, agregar_al_carrito, detalle_producto, ProductoUpdateView,   agregar_producto, eliminar_producto



urlpatterns = [
    path('mouses', mouses, name='mouses'),
    path('headsets', headsets, name='headsets'),
    path('teclados', teclados, name='teclados'),
    path('agregar_carrito/<int:producto_id>', agregar_al_carrito, name='agregar_al_carrito'),
    path('agregar_producto/', agregar_producto, name='agregar_producto'),
    path('detalle/<int:producto_id>', detalle_producto, name= 'detalle_producto'),
    path('tienda/<int:pk>/editar/', ProductoUpdateView.as_view(), name='editar_producto'),
    path('tienda/eliminar/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
]