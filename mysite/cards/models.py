from django.db import models

# Create your models here.

class Card(models.Model):
    member = models.CharField(max_length=200)
    number = models.IntegerField()
    piece = models.IntegerField()
    album = models.CharField(max_length=200)
    def __str__(self):
        return str(self.number)

