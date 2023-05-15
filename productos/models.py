from django.db import models

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator
# Create your models here.
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
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=0, validators=[MaxValueValidator(9999999999)])
    def precio_formato_colombiano(self):
        return '${:,.0f}'.format(self.precio_unitario).replace(',', '.')
    cantidad=models.PositiveIntegerField(validators=[MaxValueValidator(100)], default=1,help_text="La cantidad tiene que ser menor a 100")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")

    tamano=models.ForeignKey(Tamaño,verbose_name=_("Tamaño"),on_delete=models.CASCADE)
    tipo=models.ForeignKey(Tipo,verbose_name=_("Tipo"),on_delete=models.CASCADE)

    def __str__(self):
        return"%s %s %s"%(self.id)
    class meta:
        verbose_name_plural="Producto"