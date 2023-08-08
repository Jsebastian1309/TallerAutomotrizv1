# Generated by Django 4.2 on 2023-05-03 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_servicio', models.DateField(help_text='DD/MM/AAAA', verbose_name='Fecha de Servicio')),
                ('tecnico', models.CharField(max_length=15, verbose_name='Técnico')),
                ('kilometraje', models.IntegerField(verbose_name='Kilometraje')),
                ('estado_vehiculo', models.CharField(max_length=45, verbose_name='Estado del vehiculo')),
                ('observaciones', models.CharField(max_length=45, verbose_name='Observaciones')),
            ],
            options={
                'verbose_name_plural': 'Detalle_servicios',
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre de Servicio')),
                ('descripcion', models.CharField(max_length=45, verbose_name='Descripción')),
                ('duracion', models.IntegerField(verbose_name='Duración del servicio')),
                ('tipo_servicio', models.CharField(max_length=45, verbose_name='Tipo de Servicio')),
            ],
            options={
                'verbose_name_plural': 'Servicios',
            },
        ),
    ]