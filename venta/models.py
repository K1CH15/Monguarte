from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import integer_validator,MaxLengthValidator
from usuario.models import Persona
from productos.models import Producto
from django.db.models import Q
from safedelete.models import SafeDeleteModel

#Módulo de venta
# Create your models here.
#Modelo de Venta

class Venta(SafeDeleteModel):
    fecha=models.DateTimeField(verbose_name="Fecha",auto_now_add=True)
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTICO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
    persona_vendedor = models.ForeignKey(Persona, verbose_name=_("Vendedor"), on_delete=models.CASCADE,related_name="ventas_vendedor",limit_choices_to=Q(rol=Persona.Rol.VENDEDOR))
    persona_cliente = models.ForeignKey(Persona, verbose_name=_("Cliente"), on_delete=models.CASCADE,related_name="ventas_cliente" ,limit_choices_to=Q(rol=Persona.Rol.CLIENTE))
    def __str__(self):
        return"%s %s"%(self.persona_vendedor,self.persona_cliente)
    class meta:
        verbose_name_plural="Venta"

#Modelo de Detalle Venta
class Detalle_Venta(SafeDeleteModel):
    precio_unitario = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Precio Unitario", default=0)
    cantidad_total = models.PositiveIntegerField(verbose_name="Cantidad Total", default=0)
    producto = models.ForeignKey(Producto, verbose_name=_("Producto"), on_delete=models.CASCADE,related_name="detalles_venta_producto")
    venta= models.ForeignKey(Venta, verbose_name=_("Venta"), on_delete=models.CASCADE,related_name="detalles_venta")
    def __str__(self):
        return "%s %s %s" % (self.cantidad_total, self.precio_unitario, self.venta)

    class meta:
        verbose_name_plural = "Detalle Venta"

    def precio_unitario_colombiano(self):
        return '${:,.0f}'.format(self.precio_unitario).replace(',', '.')
