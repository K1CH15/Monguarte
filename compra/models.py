from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator
from usuario.models import Persona,Comision
from inventario.models import Materia_Prima
from django.db.models import Q
# Create your models here.
#Modelo de Compra
class Compra(models.Model):
    fecha = models.DateTimeField(verbose_name="Fecha de Compra",auto_now_add=True)
    #valor_total_compra = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MaxValueValidator(9999999999)], verbose_name="Valor total")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado = models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")

    persona_admin=models.ForeignKey(Persona,verbose_name="Administrador", on_delete=models.CASCADE,related_name="compras_administrador",limit_choices_to=Q(rol=Persona.Rol.ADMINISTRADOR))
    persona_proveedor= models.ForeignKey(Persona, verbose_name="Proveedor", on_delete=models.CASCADE,related_name="compras_proveedor",limit_choices_to=Q(rol=Persona.Rol.PROVEEDOR))
    def __str__(self):
        return"%s %s"%(self.persona_admin,self.persona_proveedor)
    class meta:
        verbose_name_plural="Compra"
#Modelo de Detalle_Compra
class Detalle_Compra(models.Model):
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=2, validators=[MaxValueValidator(9999999999)], verbose_name="Precio Unitario")
    def precio_formato_colombiano(self):
        return '${:,.0f}'.format(self.precio_unidad).replace(',', '.')
    cantidad=models.PositiveIntegerField(validators=[MaxValueValidator(100)], default=0,help_text="La cantidad tiene que ser menor a 100")
    # Campo para almacenar el valor total calculado
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Valor Total",
                                      editable=False)

    def valor_total_formato_colombiano(self):
        return '${:,.0f}'.format(self.valor_total).replace(',', '.')

    materia_prima = models.ForeignKey(Materia_Prima, verbose_name="Materia Prima", on_delete=models.CASCADE)
    compra=models.ForeignKey(Compra,verbose_name="Compra", on_delete=models.CASCADE)
    def __str__(self):
        return"%s"%(self.cantidad)
    def save(self, *args, **kwargs):
        # Obtenemos la cantidad antes de guardar el detalle de compra
        cantidad_nueva = self.cantidad

        # Calculamos el valor total multiplicando el precio_unidad por la cantidad
        self.valor_total = self.precio_unidad * cantidad_nueva

        # Guardamos el detalle de compra antes de actualizar el stock de la materia prima
        super(Detalle_Compra, self).save(*args, **kwargs)

        # Actualizamos el stock de la materia prima asociada
        if self.materia_prima:
            self.materia_prima.stock += cantidad_nueva
            self.materia_prima.save()

    class Meta:
        verbose_name_plural = "Detalle Compra"
 