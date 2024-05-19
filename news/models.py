from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    # news_crawl = models.ForeignKey(NewsCrawl, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"