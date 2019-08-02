from django.db import models


class Blogs(models.Model):
    title = models.CharField(max_length=255)
    Publication_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    Body = models.TextField()
