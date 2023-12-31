# Generated by Django 4.1.7 on 2023-07-24 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('facturacion', '0022_alter_detallefactura_venta'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='usuario',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AlterField(
            model_name='detallefactura',
            name='venta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='facturacion.venta', verbose_name='Venta'),
        ),
    ]
