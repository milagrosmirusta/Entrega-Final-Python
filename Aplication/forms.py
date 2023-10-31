from django import forms

class ClienteFormulario(forms.Form):
    nombre_completo = forms.CharField(max_length=50)
    direccion_mail = forms.CharField(max_length=50)
    telefono = forms.IntegerField()

class ProveedorFormulario(forms.Form):
    nombre_proveedor = forms.CharField(max_length=50)
    mail_proveedor = forms.CharField(max_length=50)
    telefono_prov = forms.IntegerField()


class ProductoFormulario(forms.Form):
    producto = forms.CharField(max_length=50)
    rubro = forms.CharField(max_length=50)
    subrubro = forms.IntegerField()


class BusquedaproductoFormulario(forms.Form):
    producto = forms.CharField(max_length=50, required=False)