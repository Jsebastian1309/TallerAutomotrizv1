# Generated by Django 4.1.7 on 2023-05-09 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0013_alter_venta_factura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='estado',
            field=models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=3, verbose_name='Estado'),
        ),
    ]
