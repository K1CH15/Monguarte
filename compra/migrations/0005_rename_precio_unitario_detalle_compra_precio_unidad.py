# Generated by Django 4.2.2 on 2023-10-02 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0004_rename_precio_unidad_detalle_compra_precio_unitario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detalle_compra',
            old_name='precio_unitario',
            new_name='precio_unidad',
        ),
    ]
