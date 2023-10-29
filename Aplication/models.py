from django.db import models

class Cliente(models.Model):
    nombre_completo = models.CharField(max_length=50)
    dir_mail = models.CharField(max_length=50)
    tel = models.IntegerField()

    def __str__ (self):
        return f'{self.nombre_completo}'


class Proveedor(models.Model):
    nombre_prov = models.CharField(max_length=50)
    mail_prov = models.CharField(max_length=50)
    tel_prov = models.IntegerField()

    def __str__ (self):
        return f'{self.nombre_prov}'


class Producto(models.Model):
    producto = models.CharField(max_length=50)
    rubro = models.CharField(max_length=50)
    subrubro = models.IntegerField()

    def __str__ (self):
        return f'{self.producto} {self.rubro} {self.subrubro}'
