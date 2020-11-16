from django.db import models
from django.conf import settings

class Meme(models.Model):
    title = models.CharField(max_length=70, blank=False, default="")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default=False)
