# Generated by Django 4.1.5 on 2023-08-08 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0008_rename_nombre_servicio_nombreservicio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='duracion',
            field=models.DurationField(verbose_name='Duración de la cita'),
        ),
    ]
