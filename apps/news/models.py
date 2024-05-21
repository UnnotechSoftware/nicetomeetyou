from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    url = models.TextField(default='Missing', unique=True)  # as unique
    report_datetime = models.DateTimeField(auto_now=True)
    author_name = models.CharField(max_length=255, default='Unknown Author')

    def __str__(self):
        return f"{self.title}"