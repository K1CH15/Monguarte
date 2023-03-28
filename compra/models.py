from django.db import models
#Módulo de compra
# Create your models here.
#Modelo de Detalle_Compra
class Detalle_Compra(models.Model):
    id_detalle_compra=models.AutoField(primary_key=True,verbose_name="Id Detalle Compra")
    descripcion=models.TextField(max_length=100,verbose_name="Descripción")
    precio_unidad=models.FloatField(max_length=10,verbose_name="Precio unitario")
    cantidad_total=models.IntegerField(max_length=20,verbose_name="Cantidad Total")
    id_compra=models.ForeignKey("compra.Compra", verbose_name=("Id de Compra"), on_delete=models.CASCADE)
    id_materia_prima=models.ForeignKey("stock.Materia_Prima",verbose_name="Id Materia Prima")
#Modelo de Compra
class Compra(models.Model):
    id_compra=models.AutoField(primary_key=True,verbose_name="Id de Compra")
    fecha_compra=models.DateTimeField(verbose_name="Fecha de Compra")
    valor_total=models.DecimalField(max_length=10,decimal_places=2,verbose_name="Valor total")
    numero_documento_persona=models.ForeignKey("persona.Persona",verbose_name="Número de Documento")
    id_contabilidad=models.ForeignKey("persona.Contabilidad", verbose_name=("Id contabilidad"), on_delete=models.CASCADE)