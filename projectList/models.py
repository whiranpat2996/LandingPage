from django.db import models

# Create your models here.

class project(models.Model):
    id = models.UUIDField()
    title = models.CharField()
    intro = models.CharField()
    date = models.DateField()
    abstract = models.CharField()
    steps = models.JSONField()
    pics = models.JSONField()
    vids = models.JSONField()
    conclusion = models.CharField()
