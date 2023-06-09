from django.shortcuts import render
from django.views import generic
from .models import project

# Create your views here.

class projectListView(generic.ListView):
    template_name = "projectspage.html"
    context_object_name = 'project_list'

    def get_queryset(self):
        return project.objects.all()

class projectView(generic.DetailView):
    model = project
    template_name = 'projects.html'