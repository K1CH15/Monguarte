# Generated by Django 4.2.2 on 2023-08-19 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comision',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='comision',
            name='deleted_by_cascade',
        ),
        migrations.RemoveField(
            model_name='comision',
            name='valor',
        ),
        migrations.AddField(
            model_name='comision',
            name='valor_comision',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Valor de Comisión'),
        ),
        migrations.AlterField(
            model_name='comision',
            name='fecha',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha'),
        ),
    ]