# Generated by Django 4.1.7 on 2023-10-06 13:49

from django.db import migrations, models
import servicio.models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0003_alter_servicio_kilometraje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_servicio',
            name='costoservicio',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=10, validators=[servicio.models.numeric_validator], verbose_name='Costo Servico'),
        ),
        migrations.AlterField(
            model_name='detalle_servicio',
            name='descripcion',
            field=models.CharField(default='', max_length=45, validators=[servicio.models.alphabetic_validator], verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='detalle_servicio',
            name='nombreservicio',
            field=models.CharField(default='', max_length=20, validators=[servicio.models.alphabetic_validator], verbose_name='Nombre de Servicio'),
        ),
        migrations.AlterField(
            model_name='detalle_servicio',
            name='tipo_servicio',
            field=models.CharField(default='', max_length=45, validators=[servicio.models.alphabetic_validator], verbose_name='Tipo de Servicio'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='estado_vehiculo',
            field=models.CharField(default='', max_length=45, validators=[servicio.models.alphabetic_validator], verbose_name='Estado del vehiculo'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='kilometraje',
            field=models.CharField(default=0, max_length=8, validators=[servicio.models.numeric_validator], verbose_name='Kilometraje'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='observaciones',
            field=models.CharField(default='', max_length=45, validators=[servicio.models.alphabetic_validator], verbose_name='Observaciones'),
        ),
    ]
