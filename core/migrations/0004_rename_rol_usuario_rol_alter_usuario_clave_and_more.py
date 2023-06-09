# Generated by Django 4.2 on 2023-04-18 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rol_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='Rol',
            new_name='rol',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='clave',
            field=models.CharField(default='clave', max_length=20, verbose_name='Clave'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.CharField(max_length=50, verbose_name='Correo electronico'),
        ),
    ]
