# Generated by Django 4.1.5 on 2023-08-10 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0016_alter_usuario_options_usuario_es_cliente_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='es_cliente',
        ),
    ]
