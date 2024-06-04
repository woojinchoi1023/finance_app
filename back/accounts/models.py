from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=16, blank=True)

class Following(models.Model):
    followers = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followers')
    followings = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="followings")
    created_at = models.DateTimeField(auto_now_add=True)