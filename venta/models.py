from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import integer_validator,MaxLengthValidator
from usuario.models import Persona
#Módulo de venta
# Create your models here.
#Modelo de Venta
class Venta(models.Model):
    fecha=models.DateTimeField(verbose_name="Fecha",auto_now_add=True)
    valor_total=models.DecimalField(max_digits=6,decimal_places=2,verbose_name="Valor total" ,default=0)
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTICO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
    persona=models.ForeignKey(Persona, verbose_name=_("Persona"), on_delete=models.CASCADE)

    def __str__(self):
        return"%s %s"%(self.valor_total,self.fecha)
    class meta:
        verbose_name_plural="Venta"

#Modelo de Detalle Venta
class Detalle_Venta(models.Model):
    precio_unitario=models.DecimalField(max_digits=6, decimal_places=2,verbose_name="Precio Unitario" ,default=0)
    cantidad_total = models.PositiveIntegerField(verbose_name="Cantidad Total",default=1)
    venta=models.ForeignKey(Venta, verbose_name=_("Venta"), on_delete=models.CASCADE)

    def __str__(self):
        return"%s %s"%(self.cantidad_total,self.precio_unitario,self.venta)
    class meta:
        verbose_name_plural="Detalle Venta"