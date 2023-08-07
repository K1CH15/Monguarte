from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import integer_validator,MaxLengthValidator,ValidationError,RegexValidator
#Módulo de usuarios
# Create your models here.
#Modelo Persona
# def letras_uniquemente(value):
#     if not value.isalpha():
#         raise ValidationError("El campo solo permite letras.")
class Persona(models.Model):
    class TipoDocumento(models.TextChoices):
        CC='CC ',_("Cédula de Ciudadanía")
        TI='TI',_("Tarjeta de Identidad")
        CE='CE',_("Cédula de Extranjería")
    tipo_documento=models.CharField(max_length=3,choices=TipoDocumento.choices,default=TipoDocumento.CC,verbose_name="Tipo de Documento")
    numero_documento=models.CharField(max_length=10,validators=[integer_validator],verbose_name="Número de Documento",unique=True)
    nombres=models.CharField(max_length=30,verbose_name="Nombres")
    apellidos=models.CharField(max_length=30,verbose_name="Apellidos")
    telefono=models.CharField(max_length=10,validators=[integer_validator,MaxLengthValidator(10)],verbose_name="Número Telefónico",unique=True)
    correo_electronico=models.EmailField(max_length=50,verbose_name="Correo Electrónico",unique=True)
    class Rol(models.TextChoices):
        ADMINISTRADOR='ADMI',_("Administrador")
        VENDEDOR='VEN',_("Vendedor")
        PROVEEDOR='PROV',_("Proveedor")
        CLIENTE='CLIE',_("Cliente")
    rol=models.CharField(max_length=4,choices=Rol.choices,help_text="Roles:Administrador,Vendedor,Proveedor,Cliente")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTICO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
    ips = models.CharField(max_length=10,verbose_name="IPS",blank=True,null=True)

    def __str__(self):
        return"%s %s %s %s %s %s"%("Numero De Documento:",self.numero_documento,self.nombres,self.apellidos,",Rol:",self.get_rol_display())
    class meta:
        verbose_name_plural="Persona"
#Modelo de Comisión
class Comision(models.Model):
    valor=models.DecimalField(max_digits=25, decimal_places=2, verbose_name="Valor")#puede que se deje fijo en 8mil
    fecha=models.DateTimeField(verbose_name="Fecha",auto_now_add=True)
    def precio_formato_colombiano(self):
        return '${:,.0f}'.format(self.valor).replace(',', '.')

#modelo de IPS
# class Ips(models.Model):
#
#     nombre_ips=models.CharField(max_length=20,verbose_name="Nombre")
#     class Estado(models.TextChoices):
#         ACTIVO='1',_("Activo")
#         INACTICO='0',_("Inactivo")
#     estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
#
#     def __str__(self):
#         return"%s"%(self.nombre_ips)
#     class meta:
#         verbose_name_plural="Prestador de salud"
# #Modelo de Nómina
# class Nomina(models.Model):
#
#     valor=models.DecimalField(max_digits=25, decimal_places=2, verbose_name="Valor a Pagar")
#     fecha=models.DateTimeField(verbose_name="Fecha",auto_now_add=True)
#     class Estado(models.TextChoices):
#         ACTIVO='1',_("Activo")
#         INACTICO='0',_("Inactivo")
#     estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
#     def precio_formato_colombiano(self):
#         return '${:,.0f}'.format(self.valor).replace(',', '.')
#     def __str__(self):
#         return"%s"%(self.valor)
#     class meta:
#         verbose_name_plural="Nomina"
#
# class Trabajador(models.Model):
#
#     persona=models.ForeignKey(Persona, verbose_name=_("Seleccione al Trabajador"),help_text="Recuerde que solo las personas con rol de vendedor se mostraran en los trabajadores", on_delete=models.CASCADE)
#     nomina=models.ForeignKey(Nomina, verbose_name=_("Valor a Pagar"),help_text="Valor que se le paga al trabajador", on_delete=models.CASCADE)
#     ips=models.ForeignKey(Ips, verbose_name=_("Prestador de salud"),help_text="Seleccione una IPS", on_delete=models.CASCADE)
#     def formato_colombiano(self):
#         return '${:,.0f}'.format(self.nomina.valor).replace(',', '.')
