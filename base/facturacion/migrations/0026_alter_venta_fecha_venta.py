# Generated by Django 4.1.7 on 2023-07-24 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0025_remove_detallefactura_vehiculo_detallefactura_venta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha_venta',
            field=models.DateField(help_text='DD/MM/AAAA', verbose_name='Fecha de Venta'),
        ),
    ]
