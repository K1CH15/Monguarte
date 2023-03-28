from django.db import models
#Módulo de venta
# Create your models here.
#Modelo de Cliente
class Cliente(models.Models):
    registro=models.IntegerField(max_length=25,verbose_name="Numero de registro")
    class TipoDocumento(models.TextChoices):
        CC='1',("Cédula de Ciudadanía")
        TI='2',("Tarjeta de Identidad")
        CE='3',("Cédula de Extranjería")
    tipo_documento=models.CharField(max_length=1,choices=TipoDocumento.choices,default=TipoDocumento.CC,verbose_name="Tipo de Documento")
    numero_documento_cliente=models.IntegerField(primary_key=True,max_length=20,verbose_name="Numero de documento del cliente")
    nombre=models.CharField(max_length=45,verbose_name="Nombre")
    apellido=models.CharField(max_length=45,verbose_name="Apellido")
    numero_telefono=models.IntegerField(max_length=10,verbose_name="Numero Telefónico")
    direccion=models.CharField(max_length=50,verbose_name="Dirección")
#Modelo de Venta
class Venta(models.Model):
    id_venta=models.AutoField(primary_key=True,)
    fecha=models.DateTimeField(verbose_name="Fecha")
    valor_total=models.DecimalField(max_length=10,decimal_places=2,verbose_name="Valor total")
    numero_documento_cliente=models.ForeignKey("venta.Cliente",verbose_name="Número Documento Cliente")
    numero_documento_persona=models.ForeignKey("persona.Persona",verbose_name="Número de Documento Persona")
#Modelo de Detalle Venta
class Detalle_Venta(models.Models):
    id_detale_venta=models.AutoField(primary_key=True)
    descrpicion=models.TextField(max_length=100,verbose_name="Descripción")
    cantidad_total=models.IntegerField(max_length=20,verbose_name="Cantidad Total")
    precio_unitario=models.FloatField(max_length=10,verbose_name="Precio Unitario")
    id_venta=models.ForeignKey()
    id_stock_producto=models.ForeignKey()