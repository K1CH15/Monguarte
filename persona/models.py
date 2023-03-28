from django.db import models
#Módulo de persona
# Create your models here.
#Modelo Persona
class Persona(models.Model):
    registro=models.IntegerField(max_length=45,verbose_name="N° de registro")
    class TipoDocumento(models.TextChoices):
        CC='1',("Cédula de Ciudadanía")
        TI='2',("Tarjeta de Identidad")
        CE='3',("Cédula de Extranjería")
    tipo_documento=models.CharField(max_length=1,choices=TipoDocumento.choices,default=TipoDocumento.CC,verbose_name="Tipo de Documento")
    numero_documento_persona=models.IntegerField(primary_key=True,max_length=20,verbose_name="Número de Documento Persona")
    nombre_persona=models.CharField(max_length=45,verbose_name="Nombre")
    apellido_persona=models.CharField(max_length=45,verbose_name="Apellido")
    numero_telefono=models.IntegerField(max_length=10,verbose_name="Número Telefónico")
    class  Rol(models.TextChoices):
        administrador=("Administardor")
        empleado=("Empleado")
    rol=models.CharField(max_length=1,choices=Rol.choices,default=Rol.empleado,)
    correo_persona=models.EmailField(max_length=100)
    
#modelo de IPS
class Ips(models.Model):
    id_ips=models.AutoField(primary_key=True,verbose_name="Id IPS")
    nombre_ips=models.CharField(max_length=50,verbose_name="Nombre")
    numero_documento_persona=models.ForeignKey("persona.Persona", verbose_name=("Número de Documento Persona"), on_delete=models.CASCADE)
    
#Modelo de Nómina
class Nomina(models.Model):
    id_nomina=models.AutoField(primary_key=True,verbose_name="Id Nómina")
    valor_pagar=models.FloatField(max_length=25,verbose_name="Valor a Pagar")
    numero_documento_persona=models.ForeignKey("persona.Persona", verbose_name=("Número de Documento Persona"), on_delete=models.CASCADE)
    
#Modelo de Contabilidad
class Contabilidad(models.Model):
    id_contabilidad=models.AutoField(primary_key=True,verbose_name="Id Registro Contable")
    descripcion=models.TextField(max_length=100,verbose_name="Descripción")
    cantidad_aporte=models.FloatField(max_length=25,verbose_name="Aporte")#puede que se deje fijo en 8mil
    fecha_pago=models.DateTimeField(verbose_name="Fecha de Pago")
    numero_documento_persona=models.ForeignKey("persona.Persona", verbose_name=("Número de Documento Persona"), on_delete=models.CASCADE)