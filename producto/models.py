from django.db import models
from django.utils.translation import gettext_lazy as _
#Modelo del módulo Productos
# Create your models here.
class Producto(models.Model):
    #Modelo de producto
    id_producto=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=45,verbose_name="Nombre")
    precio_unidad=models.FloatField(max_length=10,verbose_name="Precio unitario")
    cantidad=models.IntegerField(max_length=10,verbose_name="Cantidad")
    #id_tipo_producto=models.ForeignKey()
    #id_tamaño_producto=models.ForeignKey()
    #id_stock_producto=models.ForeignKey(")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTICO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")

#Modelo de Tipo de Producto
class Tipo_Producto(models.Model):
    
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30,verbose_name="Tipo de Producto")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTICO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
#Modelo de Tamaño Producto
class Tamaño_Producto(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30,verbose_name="Tamaño")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTICO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")