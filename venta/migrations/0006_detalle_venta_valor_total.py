# Generated by Django 4.2.2 on 2023-10-10 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0005_remove_detalle_venta_valor_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle_venta',
            name='valor_total',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10, verbose_name='Valor Total'),
        ),
    ]
