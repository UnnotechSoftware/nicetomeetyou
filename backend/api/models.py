from django.db import models


class News(models.Model):
    pid = models.BigAutoField(null=False, primary_key=True, auto_created=True)
    story_id = models.FloatField(null=False, unique=True)
    headline = models.CharField(null=False, max_length=30, unique=True)
    image = models.TextField(null=False)
    author = models.CharField(null=False, max_length=30)
    publisher = models.CharField(null=False, max_length=30)
    context = models.TextField(null=False)
    date_published = models.DateTimeField()
    date_modified = models.DateTimeField()

    def __str__(self):
        return self.headline
