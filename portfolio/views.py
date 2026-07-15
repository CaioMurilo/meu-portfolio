from django.shortcuts import render, get_object_or_404
from .models import Profile, Project, HomeSection, Page

def index(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    sections = HomeSection.objects.all()
    pages = Page.objects.all()
    
    return render(request, 'portfolio/index.html', {
        'profile': profile, 'projects': projects, 'sections': sections, 'pages': pages,
    })

def page_detail(request, slug):
    profile = Profile.objects.first()
    page = get_object_or_404(Page, slug=slug)
    pages = Page.objects.all()
    return render(request, 'portfolio/page.html', {'page': page, 'pages': pages, 'profile': profile})

# NOVA FUNÇÃO
def project_detail(request, slug):
    profile = Profile.objects.first()
    project = get_object_or_404(Project, slug=slug)
    pages = Page.objects.all()
    return render(request, 'portfolio/project.html', {'project': project, 'pages': pages, 'profile': profile})

def projects_list(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    pages = Page.objects.all()
    
    return render(request, 'portfolio/projects.html', {
        'profile': profile, 
        'projects': projects, 
        'pages': pages
    })