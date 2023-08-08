# Generated by Django 4.2.4 on 2023-08-06 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_alter_usuario_options_usuario_arl_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='arl',
            field=models.ForeignKey(blank=True, limit_choices_to={'usuario__tipo_usuario__in': ['Administrador', 'Mecanico', 'Secretaria']}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.arl', verbose_name='ARL'),
        ),
    ]