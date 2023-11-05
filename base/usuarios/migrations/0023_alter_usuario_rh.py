# Generated by Django 4.1.5 on 2023-10-19 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0022_alter_usuario_rh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rh',
            field=models.CharField(blank=True, choices=[('OP', 'O+'), ('ON', 'O-'), ('AP', 'A+'), ('AN', 'A-'), ('BP', 'B+'), ('BN', 'B-'), ('ABP', 'AB+'), ('ABN', 'AB-')], max_length=3, verbose_name='Factor RH'),
        ),
    ]