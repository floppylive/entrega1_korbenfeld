# Generated by Django 4.1.7 on 2023-05-31 02:40

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_infoextra_frase_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infoextra',
            name='frase_descripcion',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
