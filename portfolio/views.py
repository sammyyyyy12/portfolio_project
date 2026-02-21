from django.shortcuts import render
from .models import Project, Resume, Poem


def home(request):
    resume = Resume.objects.filter(is_active=True).first()
    projects = Project.objects.all()
    poem = Poem.objects.filter(is_active=True).first()

    return render(request, 'portfolio/home.html', {
        'resume': resume,
        'projects': projects,
        'poem': poem
    })


def about(request):
    poem = Poem.objects.filter(is_active=True).first()

    return render(request, 'portfolio/about.html', {
        'poem': poem
    })


def projects(request):
    projects = Project.objects.all()

    return render(request, 'portfolio/projects.html', {
        'projects': projects
    })
