# Generated by Django 4.1.7 on 2023-07-21 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0006_alter_linea_estado_alter_vehiculo_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='linea',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vehiculo.linea', verbose_name='Linea del Vehiculo'),
        ),
    ]
