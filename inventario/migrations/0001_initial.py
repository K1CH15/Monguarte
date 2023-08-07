
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unidad_Medida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese el Nombre de la Unidad de Medida', max_length=20, unique=True, verbose_name='Nombre de la Unidad de Medida')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
            ],
            options={
                'verbose_name_plural': 'Unidad Medida',
            },
        ),
        migrations.CreateModel(
            name='Materia_Prima',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese el Nombre de la Materia Prima', max_length=20, verbose_name='Nombre de la Materia Prima')),
                ('tipo', models.CharField(choices=[('1', 'Cera'), ('2', 'Esparto'), ('3', 'Lana')], max_length=3, verbose_name='Tipo de Materia Prima')),
                ('color', models.CharField(max_length=20, verbose_name='Color Materia Prima')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('unidad_medida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.unidad_medida', verbose_name='Unidad de Medida')),
            ],
            options={
                'verbose_name_plural': 'Materia Prima',
            },
        ),
        migrations.CreateModel(
            name='Fabricacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Fabricación')),
                ('cantidad_producto', models.PositiveIntegerField(default=0, help_text='La cantidad tiene que ser menor a 100', validators=[django.core.validators.MaxValueValidator(100)])),
                ('cantidad_materia', models.PositiveIntegerField(default=0, help_text='cantidad utilizada para hacer el producto', validators=[django.core.validators.MaxValueValidator(100)])),
                ('materia_prima', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.materia_prima', verbose_name='Materia Prima')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto', verbose_name='Producto')),
            ],
            options={
                'verbose_name_plural': 'Fabricación',
            },
        ),
    ]
