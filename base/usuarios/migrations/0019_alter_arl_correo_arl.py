# Generated by Django 4.1.5 on 2023-08-14 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0018_alter_usuario_tipo_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arl',
            name='correo_arl',
            field=models.EmailField(max_length=50, verbose_name='Correo Arl'),
        ),
    ]
