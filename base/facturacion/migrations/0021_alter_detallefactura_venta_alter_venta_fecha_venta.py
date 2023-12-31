# Generated by Django 4.1.7 on 2023-07-24 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0020_alter_venta_fecha_venta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallefactura',
            name='venta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='facturacion.venta', verbose_name='ventas'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha_venta',
            field=models.DateTimeField(help_text='DD/MM/AAAA', verbose_name='Fecha de Venta'),
        ),
    ]
