# Generated by Django 4.1.5 on 2023-08-14 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0004_alter_cita_descripcion_cita_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mantenimiento',
        ),
    ]