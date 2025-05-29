from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class VideoHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='video_history')
    video_id = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    thumbnail_url = models.URLField()
    channel_title = models.CharField(max_length=255)
    duration = models.CharField(max_length=50)
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-viewed_at']
        verbose_name_plural = 'Video histories'

    def __str__(self):
        return f"{self.user.username} - {self.title}"
