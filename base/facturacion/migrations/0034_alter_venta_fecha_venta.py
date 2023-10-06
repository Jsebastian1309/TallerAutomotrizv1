# Generated by Django 4.1.7 on 2023-10-06 13:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0033_alter_venta_fecha_venta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha_venta',
            field=models.DateTimeField(default=datetime.date.today, help_text='DD/MM/AAAA', verbose_name='Fecha de Venta'),
        ),
    ]
