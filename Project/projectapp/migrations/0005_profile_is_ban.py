# Generated by Django 4.1 on 2022-08-26 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0004_video_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_ban',
            field=models.BooleanField(default=False),
        ),
    ]
