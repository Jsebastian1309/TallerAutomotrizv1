# Generated by Django 4.1.5 on 2023-08-08 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0014_usuario_confirmarcontraseña_usuario_contraseña_and_more'),
        ('vehiculo', '0016_alter_linea_options_alter_vehiculo_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='identificacion',
            field=models.ForeignKey(default=None, limit_choices_to={'tipo_usuario': 'Cliente'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario', verbose_name=' Nombre Cliente'),
        ),
    ]