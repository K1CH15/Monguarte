# Generated by Django 4.2 on 2023-05-15 00:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tamaño',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Tamaño')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Tipo')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45, verbose_name='Nombre')),
                ('precio_unitario', models.DecimalField(decimal_places=0, max_digits=10, validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('cantidad', models.PositiveIntegerField(default=1, help_text='La cantidad tiene que ser menor a 100', validators=[django.core.validators.MaxValueValidator(100)])),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('tamano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.tamaño', verbose_name='Tamaño')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.tipo', verbose_name='Tipo')),
            ],
        ),
    ]
