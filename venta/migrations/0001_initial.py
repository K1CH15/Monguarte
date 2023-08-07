

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('persona_cliente', models.ForeignKey(limit_choices_to=models.Q(('rol', 'CLIE')), on_delete=django.db.models.deletion.CASCADE, related_name='ventas_cliente', to='usuario.persona', verbose_name='Cliente')),
                ('persona_vendedor', models.ForeignKey(limit_choices_to=models.Q(('rol', 'VEN')), on_delete=django.db.models.deletion.CASCADE, related_name='ventas_vendedor', to='usuario.persona', verbose_name='Vendedor')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_unitario', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Precio Unitario')),
                ('cantidad_total', models.PositiveIntegerField(default=0, verbose_name='Cantidad Total')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles_venta_producto', to='productos.producto', verbose_name='Producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles_venta', to='venta.venta', verbose_name='Venta')),
            ],
        ),
    ]
