from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    email = models.CharField(max_length=150)
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=158)
    username = models.CharField(max_length=155, unique=True)
    phone_number = models.CharField(max_length=9, null=True)
    profile_pic = models.ImageField(upload_to='users', default='default_profile_pic.png')

    def __str__(self):
        return self.username


@receiver(post_save, sender=CustomUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)