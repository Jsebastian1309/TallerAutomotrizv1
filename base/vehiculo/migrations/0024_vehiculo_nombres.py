# Generated by Django 4.1.5 on 2023-08-14 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0019_alter_arl_correo_arl'),
        ('vehiculo', '0023_alter_linea_nombre_linea_alter_vehiculo_tipo_aceite'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='nombres',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario', verbose_name=' Nombre Usuario'),
        ),
    ]
