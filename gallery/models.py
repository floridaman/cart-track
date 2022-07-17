from django.db import models
from django.conf import settings
from django.utils.html import format_html


class System(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Game(models.Model):
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    boxart = models.FileField(upload_to='games/', default='games/default.png')

    def __str__(self):
        return self.name

    def boxart_tag(self):
        return format_html('<img src="%s" width="150"/>' % self.boxart.url)

class Collection(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    games = models.ManyToManyField(Game)