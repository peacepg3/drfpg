# Generated by Django 4.0.5 on 2022-06-19 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apithree', '0003_alter_songs_song_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='SONG_IMG',
            field=models.URLField(),
        ),
    ]
