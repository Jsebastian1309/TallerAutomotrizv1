# Generated by Django 4.1.7 on 2023-07-24 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0023_venta_usuario_alter_detallefactura_venta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallefactura',
            name='venta',
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='vehiculo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='facturacion.venta', verbose_name=' Vehiculo'),
        ),
    ]