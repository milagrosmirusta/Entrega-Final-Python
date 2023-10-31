from django.urls import path
from Aplication.views import vista_cliente, vista_inicio, vista_proveedor, vista_producto

urlpatterns = [
    
    path('',vista_inicio,name="inicio"),
    path('inicio/',vista_inicio,name="inicio"),
    path('cliente/',vista_cliente,name="cliente"),
    path('proveedor/',vista_proveedor,name="proveedor"),
    path('producto/',vista_producto,name="producto"),
]
