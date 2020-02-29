from django.shortcuts import render
from edoc.models import Projects

# Create your views here.
def home_view(request):
    return render(request, 'edoc/homepage.html')

def project_info_view(request):
    projects = Projects.objects.all()
    return render(request, 'edoc/result.html', {'projects':projects})