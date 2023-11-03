# Generated by Django 4.2.2 on 2023-10-11 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_persona_user_alter_persona_numero_documento_and_more'),
        ('compra', '0007_detalle_compra_valor_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='persona_admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compras_administrador', to='usuario.persona', verbose_name='Administrador'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='persona_proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compras_proveedor', to='usuario.persona', verbose_name='Proveedor'),
        ),
    ]