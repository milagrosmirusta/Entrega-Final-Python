from django.db import models
from ckeditor.fields import RichTextField

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = RichTextField(default='Sin descripción')
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    imagen = models.ImageField(upload_to='productos', default='default.jpg')
    cantidad = models.IntegerField(default=0)
    tipo = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.id} - {self.nombre} - {self.descripcion} - {self.precio} - {self.cantidad} - {self.tipo}'
