# Generated by Django 4.1.7 on 2023-05-09 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0003_alter_linea_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linea',
            name='transmision',
            field=models.CharField(choices=[('Manual', 'Manual'), ('Automatico', 'Automatico')], max_length=10, verbose_name='Transmision'),
        ),
    ]
