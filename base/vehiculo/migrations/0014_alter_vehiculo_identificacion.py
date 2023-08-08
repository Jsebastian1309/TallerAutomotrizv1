# Generated by Django 4.1.5 on 2023-08-08 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0013_alter_arl_correo_arl_alter_arl_telefono_arl'),
        ('vehiculo', '0013_vehiculo_identificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='identificacion',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario', verbose_name='Usuario'),
        ),
    ]
