from django.shortcuts import render

# Create your views here.
def begin(request):
	context = {}
	current_project = Project.objects.get(pk=1)
	context['project'] = current_project
	context['status'] = "No"
	context['objectives'] = Objective.objects.filter(project=current_project)
	context['resources'] = Resource.objects.filter(project=current_project).order_by('id')
	return render(request, 'demo/step1.html', context)

def middle(request):
	context = {}
	return render(request, 'demo/step2.html', context)

def end(request):
	context = {}
	return render(request, 'demo/step3.html', context)