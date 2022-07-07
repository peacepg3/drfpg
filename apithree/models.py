from django.db import models

# Create your models here.
class Category(models.Model):
    TITLE = models.CharField(max_length=90)
    def __str__(self):
        return self.TITLE


class Songs(models.Model):
    SONG_NAME = models.CharField(max_length=90)
    SONG_CATEGORY = models.ForeignKey(Category, related_name='songs', on_delete=models.CASCADE)
    SONG_BY = models.CharField(max_length=90)
    SONG_DES = models.TextField()
    SONG_IMG = models.URLField()
    SONG_UPLODED = models.DateTimeField(auto_now_add=True)
    SONG_RATE = models.FloatField()
    FAVORITE = models.BooleanField()
    def __str__(self):
        return self.SONG_NAME

