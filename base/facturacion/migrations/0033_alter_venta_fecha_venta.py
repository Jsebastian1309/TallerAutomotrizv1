# Generated by Django 4.1.7 on 2023-10-06 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0032_alter_venta_fecha_venta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha_venta',
            field=models.DateTimeField(help_text='DD/MM/AAAA', verbose_name='Fecha de Venta'),
        ),
    ]
