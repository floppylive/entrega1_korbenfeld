# Generated by Django 4.2 on 2023-04-26 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_infoextra_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='infoextra',
            name='avatar_thumbnail',
            field=models.ImageField(default='avatares/default_thumbnail.png', upload_to='avatares/'),
        ),
    ]
