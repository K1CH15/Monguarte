# Generated by Django 4.2.2 on 2023-08-19 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fabricacion',
            name='producto',
            field=models.ForeignKey(limit_choices_to={'_safedelete': False}, on_delete=django.db.models.deletion.CASCADE, to='productos.producto', verbose_name='Producto'),
        ),
    ]
