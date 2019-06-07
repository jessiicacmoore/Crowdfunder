from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import *
from .forms import *

def home(request):
    context = {'projects': Project.objects.all()}
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def create_project(request):

    if request.method == "POST":
        form = CreateProject(request.POST)
        if form.is_valid():
            new_project = form.save(commit = False)
            new_project.owner = request.user
            new_project.save()
            return redirect('home')
    else:
        form = CreateProject()

    context = {'form': form}
    return render(request, 'create_project.html', context)
