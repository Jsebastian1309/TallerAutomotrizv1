# Generated by Django 4.1.7 on 2023-10-06 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0031_alter_venta_identificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha_venta',
            field=models.DateField(help_text='DD/MM/AAAA', verbose_name='Fecha de Venta'),
        ),
    ]
