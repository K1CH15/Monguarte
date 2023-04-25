from django.db import models
from django.utils.translation import gettext_lazy as _

from venta.models import Detalle_Venta
from compra.models import Detalle_Compra
from productos.models import Producto
# Create your models here.
class Materia_Prima(models.Model):
    nombre=models.TextField(verbose_name="Nombre de la Materia Prima", help_text="Ingrese el Nombre de la Materia Prima")
    cantidad=models.IntegerField(verbose_name="Cantidad Total")
    tipo=models.TextField(max_length=30,verbose_name="Tipo de Materia Prima")
    color=models.TextField(max_length=20,verbose_name="Color Materia Prima")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado = models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
    def __str__(self):
        return"%s %s %s %s"%(self.nombre,self.tipo,self.cantidad,self.color)
    class Meta:
        verbose_name_plural="Materia Prima"

class Stock(models.Model):
    class Tipo_stock(models.TextChoices):
        producto='producto',_("Producto")
        materia='materia',_("Materia Prima")
    tipo=models.CharField(max_length=8,choices=Tipo_stock.choices,verbose_name="tipo",help_text="Materia Prima o Producto")
    cantidad=models.IntegerField(verbose_name="Cantidad Total")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado = models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")

    producto=models.ForeignKey(Producto, verbose_name=_("Producto"), on_delete=models.CASCADE)

    def __str__(self):
        return"%s %s"%(self.tipo,self.cantidad,)
    class Meta:
        verbose_name_plural="Stock"