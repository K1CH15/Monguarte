# Generated by Django 4.2.2 on 2023-10-30 21:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0014_fabricacion_detalle_fabricacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fabricacion_detalle',
            name='cantidad_producto',
        ),
        migrations.AddField(
            model_name='fabricacion',
            name='cantidad_producto',
            field=models.PositiveIntegerField(default=0, help_text='La cantidad tiene que ser menor a 100', validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]
