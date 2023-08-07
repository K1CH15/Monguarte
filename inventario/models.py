from django.db import models
from django.utils.translation import gettext_lazy as _
from productos.models import Producto
from venta.models import Detalle_Venta
from django.core.validators import MaxValueValidator


# Create your models here.
class Unidad_Medida(models.Model):
    nombre = models.CharField(max_length=20,verbose_name="Nombre de la Unidad de Medida",help_text="Ingrese el Nombre de la Unidad de Medida", unique=True)
    class Estado(models.TextChoices):
        ACTIVO = '1', _("Activo")
        INACTIVO = '0', _("Inactivo")
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    def __str__(self):
        return "%s" % (self.nombre)
    class Meta:
        verbose_name_plural = "Unidad Medida"

class Materia_Prima(models.Model):
    nombre = models.CharField(max_length=20, verbose_name="Nombre de la Materia Prima",help_text="Ingrese el Nombre de la Materia Prima")
    class Tipos(models.TextChoices):
        CERA= '1',_("Cera")
        ESPARTO = '2',_("Esparto")
        LANA = '3',_("Lana")
    tipo = models.CharField(max_length=3,choices=Tipos.choices,verbose_name="Tipo de Materia Prima",)
    color = models.CharField(max_length=20, verbose_name="Color Materia Prima")
    class Estado(models.TextChoices):
        ACTIVO = '1', _("Activo")
        INACTIVO = '0', _("Inactivo")
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    #si la materia prima ya exite con los datos iguales simplemete se suma falta para que se sume automaticamente
    #detalle_compra=models.ForeignKey(verbose_name=_("Cantidad"),help_text="Cantidad de Materia Prima",on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(Unidad_Medida, verbose_name=_("Unidad de Medida"), on_delete=models.CASCADE)
    def __str__(self):
        return "%s %s %s %s %s %s" % ("Nombre de la Materia Prima:", self.nombre, "de Tipo:", self.get_tipo_display(), "y de Color:", self.color)
    class Meta:
        verbose_name_plural = "Materia Prima"
class Fabricacion(models.Model):
    fecha = models.DateTimeField(verbose_name="Fecha de Fabricación", auto_now_add=True)
    cantidad_producto=models.PositiveIntegerField(validators=[MaxValueValidator(100)], default=0,help_text="La cantidad tiene que ser menor a 100")
    cantidad_materia=models.PositiveIntegerField(validators=[MaxValueValidator(100)], default=0,help_text="cantidad utilizada para hacer el producto")
    materia_prima = models.ForeignKey(Materia_Prima, verbose_name=_("Materia Prima"), on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto,verbose_name="Producto",on_delete=models.CASCADE)
    def __str__(self):
        return "%s" % (self.cantidad_producto)

    class Meta:
        verbose_name_plural = "Fabricación"


# class Stock_Materia_Prima(models.Model):
#     cantidad=models.IntegerField(verbose_name="Cantidad de materia prima en stock")
#     class Estado(models.TextChoices):
#         ACTIVO='1',_("Activo")
#         INACTIVO='0',_("Inactivo")
#     estado = models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
#     materia_prima=models.ForeignKey(Materia_Prima, verbose_name=_("Materia Prima"), on_delete=models.CASCADE)
#
#     def __str__(self):
#         return"%s %s"%("la cantidad de producto es:",self.materia_prima)
#     class Meta:
#         verbose_name_plural="Stock Materia Prima"
#
# class Detalle_Producto(models.Model):
#     producto=models.ForeignKey(Producto, verbose_name=_("Productos"), on_delete=models.CASCADE)
#     stock_materia_prima=models.ForeignKey(Stock_Materia_Prima, verbose_name=_("Stock Materia Prima"), on_delete=models.CASCADE)
#     def __str__(self):
#         return"%s"%(self.id)
#     class Meta:
#         verbose_name_plural="Detalle Producto"
# class Stock_Producto(models.Model):
#     cantidad=models.IntegerField(verbose_name="Cantidad Total")
#     class Estado(models.TextChoices):
#         ACTIVO='1',_("Activo")
#         INACTIVO='0',_("Inactivo")
#     estado = models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
#     detalle_producto=models.ForeignKey(Detalle_Producto, verbose_name=_("Detalle Producto"), on_delete=models.CASCADE)
#     detalle_venta=models.ForeignKey(Detalle_Venta, verbose_name=_("Detalle venta"), on_delete=models.CASCADE)
#
#     def __str__(self):
#         return"%s %s %s"%(self.cantidad,self.detalle_producto,self.detalle_venta)
#     class Meta:
#         verbose_name_plural="Stock Producto"
