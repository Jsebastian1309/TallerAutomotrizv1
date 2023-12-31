# Generated by Django 4.2 on 2023-05-03 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_arl_options_rename_estadoarl_arl_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arl',
            name='nombre_arl',
            field=models.CharField(max_length=15, verbose_name='Nombre Arl'),
        ),
        migrations.AlterField(
            model_name='arl',
            name='telefono_arl',
            field=models.CharField(max_length=16, verbose_name='Telefono Arl'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='documento',
            field=models.CharField(max_length=10, verbose_name='Documento'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(max_length=11, verbose_name='Telefono'),
        ),
    ]
