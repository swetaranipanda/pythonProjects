from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length= 100)
    album_title=models.TextField(max_length=200)
    album_logo=models.CharField(max_length = 300)

    def __str__(self):
         return self.artist

class Song(models.Model):
    albu=models.ForeignKey(Album , on_delete=models.CASCADE)  
    file_type=models.CharField(max_length=200)
    song_title=models.CharField(max_length=200)  
    is_favorite = models.BooleanField(default= False)

    def __str__(self):
        return self.song_title