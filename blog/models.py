from django.db import models


class Blogs(models.Model):
    title = models.CharField(max_length=255)
    Publication_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    Body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.Body[:100]

    def Publication_date_pretty(self):
        return self.Publication_date.strftime('%e %B %Y')
