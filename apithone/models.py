from django.db import models

# Create your models here.
class upload(models.Model):
    identity = models.PositiveIntegerField(default=1)
    title = models.CharField(max_length=90)

    def __str__(self):
        return self.title

class song(models.Model):
    song_id = models.PositiveIntegerField(default=1)
    name = models.CharField(max_length=90)
    artist = models.CharField(max_length=90)
    des = models.TextField()
    category = models.ForeignKey(upload,related_name='upload_songs',on_delete=models.CASCADE)

    def __str__(self):
        return self.name