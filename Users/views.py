from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from Users.forms import FormularioRegistrar, FormularioEdicionPerfil, FormularioEdicionContrasena
from Users.models import  Datos




def registro(request):
  
    formulario_registro = FormularioRegistrar()
  
    if request.method == 'POST':
        formulario = FormularioRegistrar(request.POST)
        if formulario.is_valid():
            formulario.save()
            print('----------se ha registrado un usuario-----------')
            return redirect('loguin')
        else:
            print(formulario.errors)

    return render(request, 'cuenta/registro.html', {'form': formulario_registro})




def loguin(request):
  
    formulario = AuthenticationForm()
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            email = formulario.cleaned_data.get('username')
            contrasena = formulario.cleaned_data.get('password')
            print('--------------SU CUENTA ESTA ACTIVA------------')
          
            usuario = authenticate(request, username=email, password=contrasena)
            login(request, usuario)
            return redirect ('inicio')
        else:
            print('-------------NO SE HA INICIADO SESION-----------')

  
    return render(request, 'cuenta/loguin.html', {'form': formulario })




@login_required
def editar_perfil(request):
    datos_extra, created = Datos.objects.get_or_create(user=request.user)
    formulario = FormularioEdicionPerfil(
        instance=request.user,
        initial={
            'direccion': datos_extra.direccion,
            'ciudad': datos_extra.ciudad,
            'pais': datos_extra.pais,
            'telefono': datos_extra.telefono,
            'avatar': datos_extra.avatar,
            'fecha_nacimiento': datos_extra.fecha_nacimiento,
        }
    )

    if request.method == 'POST':
        formulario = FormularioEdicionPerfil(
            request.POST, request.FILES, instance=request.user
        )
        if formulario.is_valid():
            nueva_direccion = formulario.cleaned_data.get('direccion')
            nueva_ciudad = formulario.cleaned_data.get('ciudad')
            nuevo_pais = formulario.cleaned_data.get('pais')
            nuevo_telefono = formulario.cleaned_data.get('telefono')
            nuevo_avatar = formulario.cleaned_data.get('avatar')
            nueva_fecha_nacimiento = formulario.cleaned_data.get(
                'fecha_nacimiento')

            if nueva_direccion:
                datos_extra.direccion = nueva_direccion
            if nueva_ciudad:
                datos_extra.ciudad = nueva_ciudad
            if nuevo_pais:
                datos_extra.pais = nuevo_pais
            if nuevo_telefono:
                datos_extra.telefono = nuevo_telefono
            if nuevo_avatar:
                datos_extra.avatar = nuevo_avatar
            if nueva_fecha_nacimiento:
                datos_extra.fecha_nacimiento = nueva_fecha_nacimiento

            formulario.save()
            datos_extra.save()
            print('-------SU PERFIL HA SIDO MODIFICADO----------')
            return redirect('mi_perfil')

    return render(request, 'cuenta/editar_perfil.html', {'form': formulario})





def mi_perfil(request):

    return render(request,'cuenta/mi_perfil.html')

# clase vasada en vista
class CambiarContrasena(LoginRequiredMixin, PasswordChangeView):
    template_name = 'cuenta/editar_contrasena.html'
    success_url = reverse_lazy('mi_perfil')
    form_class = FormularioEdicionContrasena
