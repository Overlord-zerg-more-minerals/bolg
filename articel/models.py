from django.db import models

class Articele(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    activate = models.BooleanField(default=True)
    