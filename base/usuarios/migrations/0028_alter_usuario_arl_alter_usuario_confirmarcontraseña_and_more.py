# Generated by Django 4.1.5 on 2023-11-05 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0027_cliente_alter_usuario_tipo_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='arl',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.arl', verbose_name='ARL'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='confirmarcontraseña',
            field=models.CharField(default='', max_length=20, verbose_name='Confirmar Contraseña'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='contraseña',
            field=models.CharField(default='', max_length=20, verbose_name='Contraseña'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='correo_personal',
            field=models.EmailField(default='', max_length=50, verbose_name='Correo Personal'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(max_length=50, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombreusuario',
            field=models.CharField(default='', max_length=20, verbose_name='Nombre De Usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rh',
            field=models.CharField(choices=[('OP', 'O+'), ('ON', 'O-'), ('AP', 'A+'), ('AN', 'A-'), ('BP', 'B+'), ('BN', 'B-'), ('ABP', 'AB+'), ('ABN', 'AB-')], max_length=3, verbose_name='Factor RH'),
        ),
    ]
