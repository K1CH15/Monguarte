from django.db import models
from django.utils.translation import gettext_lazy as _
#Modelo del módulo Productos
# Create your models here.
from inventario.models import Stock
#Modelo de Tipo de Producto
class Tipo(models.Model):
    nombre=models.CharField(max_length=30,verbose_name="Tipo")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")

    def __str__(self):
        return"%s"%(self.nombre)
    class meta:
        verbose_name_plural="Tipos"

#Modelo de Tamaño Producto
class Tamaño(models.Model):

    nombre=models.CharField(max_length=30,verbose_name="Tamaño")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")

    def __str__(self):
        return"%s"%(self.nombre)
    class meta:
        verbose_name_plural="Tamaños"

#Modelo de producto
class Producto(models.Model):

    nombre=models.CharField(max_length=45,verbose_name="Nombre")
    precio_unitario=models.FloatField(max_length=10,verbose_name="Precio unitario")

    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")

    tamaño=models.ForeignKey(Tamaño,verbose_name=_("Tamaño"),on_delete=models.CASCADE)
    tipo=models.ForeignKey(Tipo,verbose_name=_("Tipo"),on_delete=models.CASCADE)

    def __str__(self):
        return"%s %s %s"%(self.nombre,self.cantidad,self.precio_unitario)
    class meta:
        verbose_name_plural="Producto"