import uuid
from django.db import models
from django.shortcuts import render
from django.template.defaultfilters import slugify

# Create your models here.

class project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1())
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=2500)
    date = models.DateField()
    abstract = models.CharField(max_length=2500)
    steps = models.JSONField(blank=True)
    pics = models.JSONField(blank=True)
    vids = models.JSONField(blank=True)
    conclusion = models.CharField(max_length=2500)

    def __str__(self):
        return self.title
    
    def slug(self):
        return slugify(self.title)
    
    def list_view(request):
        context = {}
        context["project_list"] = project.objects.all()
        return render(request, "projectspage.html", context)