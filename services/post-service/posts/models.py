from django.db import models


class Post(models.Model):
    author_id = models.IntegerField()
    author_username = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title