from django.db import models
from datetime import date
from django.contrib.auth.models import User
from Aplication.models import Producto
       


class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null= False, default=1)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=1)
    nombre_producto = models.CharField(max_length=255, null=True)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    imagen = models.ImageField(upload_to='productos', default='default.jpg')
    fecha = models.DateField(default=date.today)

    def _str_(self):
        return f' {self.nombre_producto} - {self.precio} - {self.cantidad} - {self.imagen} - {self.fecha}'    