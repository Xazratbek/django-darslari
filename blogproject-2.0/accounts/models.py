from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    yashash_manzil = models.TextField(max_length=600,null=True, blank=True)