# Generated by Django 4.1.5 on 2023-08-07 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0004_detalle_servicio_repuesto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detalle_servicio',
            old_name='repuesto',
            new_name='nombrerepuesto',
        ),
    ]