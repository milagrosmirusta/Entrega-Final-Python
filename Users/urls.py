from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from Users.views import registro, loguin, editar_perfil, mi_perfil, CambiarContrasena



urlpatterns = [
    path('registrar/', registro, name='registro'),
    path('loguin/', loguin, name='loguin'),
    path('cerrar_sesion/', LogoutView.as_view(template_name='inicio/index.html'), name='cerrar_sesion'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('mi_perfil/', mi_perfil, name='mi_perfil'),
    path('cambiar_contrasena/', CambiarContrasena.as_view(), name='cambiar_contrasena'),
]