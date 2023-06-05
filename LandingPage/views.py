from django.http import HttpResponse,FileResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic

def view(request):
        return render(request, "index.html")