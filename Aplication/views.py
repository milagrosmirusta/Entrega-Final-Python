from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from Aplication.models import Cliente, Proveedor, Producto
from Aplication.forms import ClienteFormulario, ProveedorFormulario, ProductoFormulario, BusquedaproductoFormulario



def vista_inicio(request):
    return render(request, r'Aplication\inicio.html')



def vista_cliente(request):

    if request.method == "POST":
        formulario = ClienteFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            cliente = Cliente(nombre_completo=data.get("nombre_completo"),direccion_mail=data.get("direccion_mail"),telefono=data.get("telefono"))
            cliente.save()
        else:
            return render(request, r'Aplication\cliente.html',{"formulario":formulario})        

    formulario = ClienteFormulario()
    return render(request, r'Aplication\cliente.html',{"formulario":formulario})




def vista_proveedor(request):

    if request.method == "POST":
        formulario = ProveedorFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            proveedor = Proveedor(nombre_proveedor=data.get("nombre_proveedor"),mail_proveedor=data.get("mail_proveedor"),telefono_prov=data.get("telefono_prov"))
            proveedor.save()
        else:
            return render(request, r'Aplication\proveedor.html',{"formulario":formulario})        

    formulario = ProveedorFormulario()
    return render(request, r'Aplication\proveedor.html',{"formulario":formulario})



def vista_producto(request):
    if request.method == "POST":
        formulario_crear = ProductoFormulario(request.POST)
        if formulario_crear.is_valid():
            data = formulario_crear.cleaned_data
            producto = Producto(producto=data.get("producto"), rubro=data.get("rubro"), subrubro=data.get("subrubro"))
            producto.save()
            # Deberia redirigir al usuario o mostrar un mensaje de éxito  (para la proxima)
        else:
            return render(request, 'Aplication/producto.html', {"formulario_crear": formulario_crear})

    formulario_crear = ProductoFormulario()

    if request.method == "GET":  # Cambiado para GET
        formulario_buscar = BusquedaproductoFormulario(request.GET)
        if formulario_buscar.is_valid():
            data = formulario_buscar.cleaned_data.get("producto")
            producto_buscado = Producto.objects.filter(producto__icontains=data)
        else:
            producto_buscado = Producto.objects.all()
    else:
        formulario_buscar = BusquedaproductoFormulario()
        producto_buscado = Producto.objects.all()

    return render(request, 'Aplication/producto.html', {"formulario": formulario_buscar, "producto_buscado": producto_buscado})
