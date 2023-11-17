from django.db import models
from django.contrib.auth.models import User




    
class Datos(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    telefono = models.IntegerField( null=True, blank=True)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
   
    def __str__(self):
        return f'{self.id} - {self.user} - {self.fecha_nacimiento} - {self.direccion} - {self.ciudad} - {self.pais} - {self.telefono} - {self.avatar}'
   

        