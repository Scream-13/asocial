from codecs import oem_decode
from pyexpat import model
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profileImg = models.ImageField(upload_to='profile_images', default='blank profile image.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    username = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.username.user.username

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    def __str__(self):
        return self.user
