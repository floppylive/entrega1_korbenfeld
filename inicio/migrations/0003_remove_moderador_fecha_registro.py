# Generated by Django 4.1.7 on 2023-04-28 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_delete_mensaje_delete_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moderador',
            name='fecha_registro',
        ),
    ]
