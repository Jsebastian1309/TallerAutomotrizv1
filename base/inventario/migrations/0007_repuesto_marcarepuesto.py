# Generated by Django 4.2.4 on 2023-08-07 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0006_alter_marcarepuesto_nombremarcarepuesto'),
    ]

    operations = [
        migrations.AddField(
            model_name='repuesto',
            name='marcarepuesto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.marcarepuesto', verbose_name='Marca Repuesto'),
        ),
    ]
