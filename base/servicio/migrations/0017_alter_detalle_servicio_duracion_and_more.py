# Generated by Django 4.1.5 on 2023-08-16 01:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0016_alter_servicio_fecha_servicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_servicio',
            name='duracion',
            field=models.DurationField(default=datetime.timedelta(0), verbose_name='Duración de la cita'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='fecha_servicio',
            field=models.DateField(default=datetime.date.today, help_text='MM/DD/AAAA', verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='kilometraje',
            field=models.IntegerField(default=0, verbose_name='Kilometraje'),
        ),
    ]
