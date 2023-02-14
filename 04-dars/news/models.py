from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=180)
    text = models.TextField()
    # author = models.TextField(max_length=50)

    def __str__(self):
        return self.title