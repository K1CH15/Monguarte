# Generated by Django 4.2.2 on 2023-11-01 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0015_remove_fabricacion_detalle_cantidad_producto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fabricacion',
            name='costo_fabricacion',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Costo de Fabricación'),
        ),
    ]
