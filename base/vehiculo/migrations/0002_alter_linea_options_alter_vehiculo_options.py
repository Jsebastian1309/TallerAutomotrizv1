# Generated by Django 4.1.7 on 2023-05-08 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='linea',
            options={'verbose_name_plural': ' Linea '},
        ),
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'verbose_name_plural': ' Vehiculo '},
        ),
    ]
