from django.db import models
from django.utils.translation import gettext_lazy as _
#Modulo de Stock productos
# Create your models here.
#Modelo de Stock
class Stock(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=45,verbose_name="Stock Producto")
    cantidad=models.IntegerField(max_length=10,verbose_name="Cantidad stock")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTICO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
    #id_producto=models.ForeignKey("producto.Producto",verbose_name="id Producto")
    #id_stock_materia_prima=models.ForeignKey("stock.Materia_Prima",verbose_name="Id Materia Prima")
#Modelo de Materia Prima
class Materia_Prima(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=20,verbose_name="Materia prima")
    cantidad=models.IntegerField(max_length=10,verbose_name="Cantidad")
    tipo=models.CharField( max_length=20,verbose_name="Tipo")
    color=models.CharField(max_length=20,verbose_name="Color")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTICO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")