from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.core.validators import integer_validator
from django.utils.translation import gettext_lazy as _
class Register(models.Model):
    correo = models.EmailField(max_length=45, verbose_name="Correo:")
    usuario = models.CharField(max_length=45, verbose_name="Usuario:")
    nombre = models.CharField(max_length=45, verbose_name="Nombres:")
    numero_documento = models.CharField(max_length=10, validators=[integer_validator],verbose_name="Número de Documento", unique=True)
    apellido = models.CharField(max_length=45, verbose_name="Apellidos:")
    contrasena = models.CharField(max_length=45, verbose_name="Contraseña:")
    activo = models.BooleanField(default=False)
    # class TipoDocumento(models.TextChoices):
    #     CC='CC ',_("Cédula de Ciudadanía")
    #     TI='TI',_("Tarjeta de Identidad")
    #     CE='CE',_("Cédula de Extranjería")
    # tipo_documento=models.CharField(max_length=3,choices=TipoDocumento.choices,default=TipoDocumento.CC,verbose_name="Tipo de Documento")
    #

    def clean(self):
        self.correo = self.correo.title()
        self.usuario = self.usuario.title()
        self.contrasena = self.contrasena.lower()

    def __str__(self):
        return "%s %s" % (self.correo, self.usuario)

    class Meta:
        verbose_name_plural = "Registers"
