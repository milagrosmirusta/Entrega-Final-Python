from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms.widgets import SelectDateWidget

class FormularioRegistrar(UserCreationForm):         #formulario para class Cliente del models
    username = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre de Usuario'}))
    email = forms.EmailField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1= forms.CharField(label="", required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña (al menos 8 caracteres, alfanumérica)'}))
    password2= forms.CharField(label="", required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Repetir Contraseña'}))
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {key: '' for key in fields}
        
class FormularioEdicionPerfil(UserChangeForm):
    password = None
    username = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'placeholder': 'Nombre de Usuario'}))
    email = forms.EmailField(label="",  required=False,widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    last_name = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
    fecha_nacimiento = forms.DateField(label="", required=False, widget=SelectDateWidget(attrs={'placeholder': 'Fecha de Nacimiento'}, years=range(1950, 2024)))
    direccion = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'placeholder': 'Dirección'}))
    ciudad = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'placeholder': 'Ciudad'}))
    pais = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'placeholder': 'País'}))
    telefono = forms.IntegerField(label="", required=False, widget=forms.TextInput(attrs={'placeholder': 'Teléfono'}))
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name','fecha_nacimiento', 'direccion', 'ciudad', 'pais', 'telefono', 'avatar']
        
        
class FormularioEdicionContrasena(PasswordChangeForm):
    old_password= forms.CharField(label="", required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña Vieja'}))
    new_password1= forms.CharField(label="", required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Nueva Contraseña'}))
    new_password2= forms.CharField(label="", required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar Nueva Contraseña '}))
    
    class Meta:
        model = User
        fields = ['old_password','new_password1', 'new_password2']