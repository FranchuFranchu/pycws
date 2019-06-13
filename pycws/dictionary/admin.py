from django.contrib import admin
from . import models

admin.site.register(models.Dictionary)
admin.site.register(models.Word)
admin.site.register(models.Wordlink)
