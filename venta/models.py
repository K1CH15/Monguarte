from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import integer_validator,MaxLengthValidator
#Módulo de venta
# Create your models here.
#Modelo de Venta
class Venta(models.Model):
    id=models.AutoField(primary_key=True)
    fecha=models.DateTimeField(verbose_name="Fecha",auto_now_add=True)
    valor_total=models.DecimalField(max_digits=25,decimal_places=5,verbose_name="Valor total")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTICO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
#Modelo de Detalle Venta
class Detalle_Venta(models.Model):
    id=models.AutoField(primary_key=True)
    precio_unitario=models.DecimalField(max_digits=25, decimal_places=5, verbose_name="Precio Unitario")
    cantidad_total = models.IntegerField(verbose_name="Cantidad Total")
    #id_venta=models.ForeignKey()
    #id_materia_prima=models.ForeignKey()

#Modelo llaves foraneas
#class Detalle_Venta_Venta(models.Model):
    #id_Detalle_Venta=models.ForeignKey(Detalle_Venta, on_delete=models.CASCADE, verbose_name="Detalle Venta")
    #id_Venta=models.ForeignKey(Detalle_Venta, on_delete=models.CASCADE, verbose_name="Venta")

#class Venta_Persona(models.Model):
    #id_Venta=models.ForeignKey(Venta, on_delete=models.CASCADE, verbose_name="Venta")
    #numero_documento_persona=models.ForeignKey(Persona, on_delete=models.CASCADE, verbose_name="Persona")