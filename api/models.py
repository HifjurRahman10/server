from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    avatarId = models.CharField(max_length=100)
    avatarImageURL = models.TextField()
    avatarName = models.CharField(max_length=100)
    avatarVideoURL = models.TextField()

    def __str__(self):
        return self.avatarId

class ShortVideo(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE, related_name="short_video")
    avatarId = models.ForeignKey(Avatar, on_delete=models.DO_NOTHING, related_name="short_video")
    hook = models.CharField(max_length=100)
    videoURL= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.userId