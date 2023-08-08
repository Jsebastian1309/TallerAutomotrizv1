# Generated by Django 4.1.5 on 2023-08-07 22:16

from django.db import migrations, models
import facturacion.models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0028_remove_detallefactura_venta_remove_venta_usuario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='detalleFactura',
        ),
        migrations.AlterField(
            model_name='venta',
            name='cliente',
            field=models.CharField(default='', max_length=25, validators=[facturacion.models.alphabetic_validator], verbose_name='Cliente'),
        ),
    ]