# Generated by Django 4.1.7 on 2023-05-31 02:40

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0005_frase_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frase',
            name='frase',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='frase',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
