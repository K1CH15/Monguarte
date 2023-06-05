from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import integer_validator,MaxLengthValidator
#Módulo de usuarios
# Create your models here.
#Modelo Persona
class Persona(models.Model):
    id=models.AutoField(primary_key=True)
    class TipoDocumento(models.TextChoices):
        CC='CC ',_("Cédula de Ciudadanía")
        TI='TI',_("Tarjeta de Identidad")
        CE='CE',_("Cédula de Extranjería")
    tipo_documento=models.CharField(max_length=3,choices=TipoDocumento.choices,default=TipoDocumento.CC,verbose_name="Tipo de Documento")
    numero_documento=models.CharField(max_length=10,validators=[integer_validator],verbose_name="Número de Documento")
    primer_nombre=models.CharField(max_length=20,verbose_name="Primer Nombre")
    segundo_nombre=models.CharField(max_length=20,verbose_name="Segundo Nombre")
    primer_apellido=models.CharField(max_length=20,verbose_name="Primer Apellido")
    segundo_apellido=models.CharField(max_length=20,verbose_name="Segundo Apellido")
    telefono=models.CharField(max_length=10,validators=[integer_validator,MaxLengthValidator(10)],verbose_name="Número Telefónico")
    class  Rol(models.TextChoices):
        ADMINISTRADOR='ADMI',_("Administardor")
        VENDEDOR='VEN',_("Vendedor")
        PROVEEDOR='PROV',_("Proveedor")
        CLIENTE='CLIE',_("Cliente")
    rol=models.CharField(max_length=4,choices=Rol.choices,help_text="Roles:Administrador,Vendedor,Proveedor,Cliente")
    correo_electronico=models.EmailField(max_length=50,verbose_name="Correo Electrónico")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTICO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")

#Modelo de Contabilidad
class Contabilidad(models.Model):
    id=models.AutoField(primary_key=True)
    class TipoI(models.TextChoices):
        INGRESO='1',_("Ingreso")
        EGRESO='0',_("Egreso")
    tipo=models.CharField(max_length=1,choices=TipoI.choices,default=TipoI.INGRESO,verbose_name="Ingreso o Egreso")
    valor=models.DecimalField(max_digits=25, decimal_places=5, verbose_name="Valor")#puede que se deje fijo en 8mil
    fecha=models.DateTimeField(verbose_name="Fecha de Pago",auto_now_add=True)
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTICO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
#Modelo Aporte
class Aporte(models.Model):
    id=models.AutoField(primary_key=True)
    valor=models.DecimalField(max_digits=25, decimal_places=5, verbose_name="Valor del Aporte")
    fecha=models.DateTimeField(verbose_name="Fecha de Pago",auto_now_add=True)
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTICO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
#modelo de IPS
class Ips(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=20,verbose_name="Nombre")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTICO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")

#Modelo de Nómina
class Nomina(models.Model):
    id=models.AutoField(primary_key=True)
    valor=models.DecimalField(max_digits=25, decimal_places=5, verbose_name="Valor a Pagar")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTICO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")

#Modelo Trbajador
class Trabajador (models.Model):
    id=models.AutoField(primary_key=True)
    #persona_numero_documento=models.ForeignKey()
    #id_nomina=models.ForeignKey()
    #ips=models.models.ForeignKey()
