from django.db import models

class Music(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=25)
    bpm = models.IntegerField()
    tom = models.CharField(max_length=3)
    photo = models.ImageField(upload_to='photo/%y/%m/%d/',blank=True)

    def __str__(self):
        return self.name