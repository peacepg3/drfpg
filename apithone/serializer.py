from .models import upload,song
from rest_framework import serializers
# this is the example for model serializer so it have a data base
class UploadSerilizer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.title",read_only=True)
    class Meta:
        model = song
        fields = '__all__'
        # fields = ['song_id','name','artist','des','category']
# this is the example for simple serializer so it have not a database
class SerialSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    date = serializers.DateTimeField()

