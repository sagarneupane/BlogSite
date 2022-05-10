from django.db import models


# Create your models here.

class Blog(models.Model):
    Title = models.CharField(max_length=250)
    Description = models.TextField()
