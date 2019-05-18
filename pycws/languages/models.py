from django.db import models

class Language(models.Model):
    code = models.CharField(unique=True, max_length=6)
    name = models.TextField()

class Dialect(models.Model):
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
