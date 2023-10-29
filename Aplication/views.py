from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from Aplication.models import Cliente, Proveedor, Producto
from Aplication.forms import ClienteFormulario, ProveedorFormulario, BusquedaproductoFormulario



def vista_inicio(request):
    return render(request, r'Aplication\inicio.html')



def vista_cliente(request):

    if request.method == "POST":
        formulario = ClienteFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            cliente = Cliente(nombre_completo=data.get("nombre_completo"),dir_mail=data.get("dir_mail"),tel=data.get("tel"))
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
            proveedor = Proveedor(nombre_prov=data.get("nombre_prov"),mail_prov=data.get("mail_prov"),tel_prov=data.get("tel_prov"))
            proveedor.save()
        else:
            return render(request, r'Aplication\proveedor.html',{"formulario":formulario})        

    formulario = ProveedorFormulario()
    return render(request, r'Aplication\proveedor.html',{"formulario":formulario})



def vista_producto(request):

    formulario = BusquedaproductoFormulario(request.GET)
    if formulario.is_valid():
        data = formulario.cleaned_data.get("producto")
        producto_buscado = Producto.objects.filter(producto__icontains=data)
    else:
        producto_buscado = Producto.objects.all()

    formulario = BusquedaproductoFormulario()
    return render(request, r'Aplication\producto.html',{"formulario":formulario, "producto_buscado":producto_buscado})