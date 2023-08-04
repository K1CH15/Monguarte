# Generated by Django 4.2 on 2023-08-03 20:18

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=25, verbose_name='Valor')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Pago')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_documento', models.CharField(choices=[('CC ', 'Cédula de Ciudadanía'), ('TI', 'Tarjeta de Identidad'), ('CE', 'Cédula de Extranjería')], default='CC ', max_length=3, verbose_name='Tipo de Documento')),
                ('numero_documento', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^-?\\d+\\Z'), code='invalid', message='Enter a valid integer.')], verbose_name='Número de Documento')),
                ('nombres', models.CharField(max_length=25, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=25, verbose_name='Apellidos')),
                ('telefono', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^-?\\d+\\Z'), code='invalid', message='Enter a valid integer.'), django.core.validators.MaxLengthValidator(10)], verbose_name='Número Telefónico')),
                ('correo_electronico', models.EmailField(max_length=50, unique=True, verbose_name='Correo Electrónico')),
                ('rol', models.CharField(choices=[('ADMI', 'Administrador'), ('VEN', 'Vendedor'), ('PROV', 'Proveedor'), ('CLIE', 'Cliente')], help_text='Roles:Administrador,Vendedor,Proveedor,Cliente', max_length=4)),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('ips', models.CharField(blank=True, max_length=10, null=True, verbose_name='IPS')),
            ],
        ),
    ]
