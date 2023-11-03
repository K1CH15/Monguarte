# Generated by Django 4.2.2 on 2023-10-11 00:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('usuario', '0002_remove_comision_deleted_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='persona',
            name='numero_documento',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^-?\\d+\\Z'), code='invalid', message='Enter a valid integer.'), django.core.validators.RegexValidator('^\\d+$', message='Este campo solo permite valores numericos')], verbose_name='Número de Documento'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='rol',
            field=models.ForeignKey(blank=True, help_text='Roles:Administrador,Vendedor,', null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group', verbose_name='Rol'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^-?\\d+\\Z'), code='invalid', message='Enter a valid integer.'), django.core.validators.MaxLengthValidator(10), django.core.validators.RegexValidator('^\\d+$')], verbose_name='Número Telefónico'),
        ),
    ]