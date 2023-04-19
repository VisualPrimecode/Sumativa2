# Generated by Django 4.2 on 2023-04-19 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_usuario_sexo_usuario_genero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiculo',
            name='categoria',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='clave',
            field=models.CharField(max_length=20, verbose_name='Clave'),
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Vehiculo',
        ),
    ]
