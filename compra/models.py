from django.db import models
from django.utils.translation import gettext_lazy as _
#Módulo de compra
from usuario.models import Persona
from inventario.models import Materia_Prima
# Create your models here.
#Modelo de Compra
class Compra(models.Model):
    fecha = models.DateTimeField(verbose_name="Fecha de Compra",auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Valor total")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado = models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
    persona=models.ForeignKey(Persona,verbose_name="Persona", on_delete=models.CASCADE)
    def __str__(self):
        return"%s"%(self.id)
    class meta:
        verbose_name_plural="Compra"
#Modelo de Detalle_Compra
class Detalle_Compra(models.Model):
    precio_unidad = models.DecimalField(max_digits=10,decimal_places=2,verbose_name=("Precio unitario"))
    cantidad_total = models.IntegerField(verbose_name="Cantidad Total")
    materia_prima=models.ForeignKey(Materia_Prima, verbose_name=("Materia Prima"), on_delete=models.CASCADE)
    compra=models.ForeignKey(Compra,verbose_name="Compra", on_delete=models.CASCADE)
    materia_prima=models.ForeignKey(Materia_Prima, verbose_name=_("Materia Prima"), on_delete=models.CASCADE)
    def __str__(self):
        return"%s"%(self.id)
    class meta:
        verbose_name_plural="Detalle Compra"