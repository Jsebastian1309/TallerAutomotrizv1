# Generated by Django 4.1.7 on 2023-06-29 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0014_alter_venta_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallefactura',
            name='factura',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='factura',
        ),
    ]
