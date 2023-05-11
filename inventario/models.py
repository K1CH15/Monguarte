from django.db import models
from django.utils.translation import gettext_lazy as _
from productos.models import Producto
from venta.models import Detalle_Venta
# Create your models here.

class Materia_Prima(models.Model):
    nombre=models.CharField(max_length=20,verbose_name="Nombre de la Materia Prima", help_text="Ingrese el Nombre de la Materia Prima")
    tipo=models.CharField(max_length=20,verbose_name="Tipo de Materia Prima")
    color=models.CharField(max_length=20,verbose_name="Color Materia Prima")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado = models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
    def __str__(self):
        return"%s %s %s %s %s %s "%("Materia Prima:",self.nombre,"de tipo",self.tipo,"de color",self.color)
    class Meta:
        verbose_name_plural="Materia Prima"

class Stock_Materia_Prima(models.Model):
    cantidad=models.IntegerField(verbose_name="Cantidad de materia prima en stock")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado = models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
    materia_prima=models.ForeignKey(Materia_Prima, verbose_name=_("Materia Prima"), on_delete=models.CASCADE)

    def __str__(self):
        return"%s"%(self.cantidad)
    class Meta:
        verbose_name_plural="Stock Materia Prima"

class Detalle_Producto(models.Model):
    producto=models.ForeignKey(Producto, verbose_name=_("Productos"), on_delete=models.CASCADE)
    stock_materia_prima=models.ForeignKey(Stock_Materia_Prima, verbose_name=_("Stock Materia Prima"), on_delete=models.CASCADE)
    def __str__(self):
        return"%s"%(self.id)
    class Meta:
        verbose_name_plural="Detalle Producto"
class Stock_Producto(models.Model):
    cantidad=models.IntegerField(verbose_name="Cantidad Total")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado = models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
    detalle_producto=models.ForeignKey(Detalle_Producto, verbose_name=_("Detalle Producto"), on_delete=models.CASCADE)
    detalle_venta=models.ForeignKey(Detalle_Venta, verbose_name=_("Detalle venta"), on_delete=models.CASCADE)

    def __str__(self):
        return"%s"%(self.id)
    class Meta:
        verbose_name_plural="Stock Producto"