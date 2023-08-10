# Generated by Django 4.1.5 on 2023-08-10 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0018_alter_vehiculo_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='marca',
            field=models.CharField(choices=[('RENAULT', 'Renault'), ('CHEVROLET', 'Chevrolet'), ('HONDA', 'Honda'), ('CITROEN', 'Citroën'), ('FORD', 'Ford'), ('HYUNDAI', 'Hyundai'), ('KIA', 'Kia'), ('MAZDA', 'Mazda'), ('MITSUBISHI', 'Mitsubishi'), ('NISSAN', 'Nissan')], default='', max_length=10, verbose_name='Marca'),
        ),
    ]
