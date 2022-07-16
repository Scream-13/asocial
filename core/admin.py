from django.contrib import admin
from .models import LikePost, Profile, Post, FollowersCount
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User 

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)

