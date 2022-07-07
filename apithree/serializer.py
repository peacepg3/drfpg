from .models import Category,Songs
from rest_framework import serializers

class CategSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('TITLE','id')

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = (
            'id',
            'SONG_NAME',
            'SONG_CATEGORY',
            'SONG_BY',
            'SONG_IMG',
            'SONG_UPLODED',
            'SONG_RATE',
            'FAVORITE',
        )