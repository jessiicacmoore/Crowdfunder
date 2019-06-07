from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from crowdfunder.forms import LoginForm
from .models import *
from .forms import *

def home(request):
    return render(request, 'index.html', {
        'projects': Project.objects.all().order_by('-id')[:9]
    })

def profile(request, user_id):
    user = User.objects.get(id=user_id)
    owned_projects = user.projects.all()
    # backed_projects = [d.project for d in user.donations.all()]
    donations = user.donations.all()

    return render(request, "profile.html", {
        'user': user,
        'owned_projects': owned_projects,
        'donations': donations
    })

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=username, password=pw)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('')
            else:
                form.add_error('username', 'Login failed')
    else:
        form = LoginForm()

    context = {'form': form}
    http_response = render(request, 'login.html', context)
    return HttpResponse(http_response)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('')

def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            
            login(request, user)
            new_profile = Profile.objects.create(name=user.name, user=user)
            new_profile.save()
            return HttpResponseRedirect('')
    else:
        form = UserCreationForm()
    html_response =  render(request, 'signup.html', {'form': form})
    return HttpResponse(html_response)

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

def donate(request, id):
    project = get_object_or_404(Project, pk=id)

    if request.method == "POST":
        form = MakeDonation(request.POST)
        if form.is_valid():
            new_donation = form.save(commit = False)
            new_donation.user = request.user
            new_donation.project = project
            new_donation.save()
            project.update_donation_stats()

            return redirect('home')
    else:
        form = MakeDonation()

    context = {'form': form, 'project': project}
    return render(request, 'make_donation.html', context)
    
def profile_view(request):
    context = {'profiles': Profile.objects.all()}
    response = render(request, 'profile.html', context)
    return HttpResponse(response)
