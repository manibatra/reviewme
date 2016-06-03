from django.shortcuts import render
from projects.models import Project, Objective, Resource
from django.conf import settings

# Create your views here.
def begin(request):
	context = {}
	context['media'] = settings.MEDIA_URL
	current_project = Project.objects.get(pk=1)
	context['project'] = current_project
	context['status'] = "No"
	context['objectives'] = Objective.objects.filter(project=current_project)
	context['resources'] = Resource.objects.filter(project=current_project).order_by('id')
	return render(request, 'demo/step1.html', context)


def end(request):
	context = {}
	return render(request, 'demo/step3.html', context)