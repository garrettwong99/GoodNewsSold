from django.db import models

class Source(models.Model):
    name = models.CharField(max_length=100)  # Name of the news source
    rss_url = models.URLField(unique=True)   # RSS feed URL
    added_on = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return self.name