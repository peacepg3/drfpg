# Generated by Django 4.0.5 on 2022-06-21 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apithree', '0005_alter_songs_song_img_alter_songs_song_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='SONG_IMG',
            field=models.URLField(),
        ),
    ]
