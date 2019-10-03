from django.db import models
from users.models import UserProfile

class Language(models.Model):
    code = models.CharField(unique=True, max_length=6)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)

class Dialect(models.Model):
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
