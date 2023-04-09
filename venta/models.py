from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import integer_validator,MaxLengthValidator
#Módulo de venta
# Create your models here.

#Modelo de Venta
class Venta(models.Model):
    id=models.AutoField(primary_key=True)
    fecha=models.DateTimeField(verbose_name="Fecha",auto_now_add=True)
    valor_total=models.DecimalField(max_length=10,decimal_places=2,verbose_name="Valor total")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTICO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")


    #numero_documento_persona=models.ForeignKey()

#Modelo de Detalle Venta
class Detalle_Venta(models.Models):
    id=models.AutoField(primary_key=True)
    precio_unitario=models.DecimalField(max_digits=25, decimal_places=5, verbose_name="Precio Unitario")
    cantidad_total = models.IntegerField(verbose_name="Cantidad Total")
    #id_venta=models.ForeignKey()
    #id_materia_prima=models.ForeignKey()