from django import forms

class ClienteFormulario(forms.Form):
    nombre_completo = forms.CharField(max_length=50)
    dir_mail = forms.CharField(max_length=50)
    tel = forms.IntegerField()


class ProveedorFormulario(forms.Form):
    nombre_prov = forms.CharField(max_length=50)
    mail_prov = forms.CharField(max_length=50)
    tel_prov = forms.IntegerField()

class BusquedaproductoFormulario(forms.Form):
    producto = forms.CharField(max_length=50, required=False)