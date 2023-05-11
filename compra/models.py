from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator
from usuario.models import Persona
from inventario.models import Materia_Prima
# Create your models here.
#Modelo de Compra
class Compra(models.Model):
    fecha = models.DateTimeField(verbose_name="Fecha de Compra",auto_now_add=True)
    valor_total_compra = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MaxValueValidator(9999999999)], verbose_name="Valor total")
    def precio_formato_colombiano(self):
        return '${:,.0f}'.format(self.valor_total_compra).replace(',', '.')
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado = models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
    persona=models.ForeignKey(Persona,verbose_name="Persona", on_delete=models.CASCADE)
    def __str__(self):
        return"%s %s "%(self.persona,self.valor_total_compra)
    class meta:
        verbose_name_plural="Compra"
#Modelo de Detalle_Compra
class Detalle_Compra(models.Model):
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=2, validators=[MaxValueValidator(9999999999)], verbose_name="Valor total")
    def precio_formato_colombiano(self):
        return '${:,.0f}'.format(self.precio_unidad).replace(',', '.')
    cantidad=models.PositiveIntegerField(validators=[MaxValueValidator(100)], default=1,help_text="La cantidad tiene que ser menor a 100")
    materia_prima=models.ForeignKey(Materia_Prima, verbose_name=("Seleccione la Materia Prima"), on_delete=models.CASCADE)
    compra=models.ForeignKey(Compra,verbose_name="Seleccione quien realizo la compra", on_delete=models.CASCADE)


    def __str__(self):
        return"%s %s"%(self.materia_prima,self.cantidad)
    class meta:
        verbose_name_plural="Detalle Compra"
 