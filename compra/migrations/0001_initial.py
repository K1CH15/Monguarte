
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Compra')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('persona_admin', models.ForeignKey(limit_choices_to=models.Q(('rol', 'ADMI')), on_delete=django.db.models.deletion.CASCADE, related_name='compras_administrador', to='usuario.persona', verbose_name='Administrador')),
                ('persona_proveedor', models.ForeignKey(limit_choices_to=models.Q(('rol', 'PROV')), on_delete=django.db.models.deletion.CASCADE, related_name='compras_proveedor', to='usuario.persona', verbose_name='Proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_unidad', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name='Precio Unitario')),
                ('cantidad', models.PositiveIntegerField(default=0, help_text='La cantidad tiene que ser menor a 100', validators=[django.core.validators.MaxValueValidator(100)])),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compra.compra', verbose_name='Compra')),
            ],
        ),
    ]
