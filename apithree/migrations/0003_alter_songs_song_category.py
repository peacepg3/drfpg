# Generated by Django 4.0.5 on 2022-06-19 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apithree', '0002_alter_songs_song_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='SONG_CATEGORY',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='apithree.category'),
        ),
    ]