# Generated by Django 4.1.5 on 2023-10-26 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0025_alter_usuario_options_alter_arl_fecha_inicioafi_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name_plural': 'usuarios'},
        ),
    ]