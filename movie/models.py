from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/genres/{self.id}/"

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre) 
    release_year = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/movies/{self.id}/" 
