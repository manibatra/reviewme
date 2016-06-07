from django.shortcuts import render
from projects.models import Project, Objective, Resource
from .models import Intro
from django.conf import settings
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError




# Create your views here.
def begin(request):
	context = {}
	context['media'] = settings.MEDIA_URL
	current_project = Project.objects.order_by('id').first()
	context['project'] = current_project
	context['status'] = "No"
	context['objectives'] = Objective.objects.filter(project=current_project)
	context['resources'] = Resource.objects.filter(project=current_project).order_by('id')
	return render(request, 'demo/step1.html', context)

def start_intro(request):
	#add redirect to view intro if user already has intro object
	return render(request, 'demo/startintro.html')

def submit_intro(request):
	if request.method == 'POST':
		if request.user.is_authenticated():
			user = User.objects.get(pk=request.user.id)
			try:
				user_intro = Intro(user=user, q_a=request.POST['goal'], q_b=request.POST['inspire'], note=request.POST['note'])
				user_intro.save()
			except IntegrityError as e:
				return render(request, 'demo/viewintro.html')
			messages.add_message(request, messages.SUCCESS, 'Your project has been submitted.')
			return render(request, 'demo/viewintro.html')
		else:
			context = {}
			context['q_a'] = request.POST['goal']
			context['q_b'] = request.POST['inspire']
			context['note'] = request.POST['note']
			context['message'] = 'Thanks for filling up the project. Now signup to get the feedback'
			return render(request, 'users/signup.html', context)
	else:
		raise Http404()

def view_intro(request):
	if request.user.is_authenticated():
		user = User.objects.get(pk=request.user.id)
		try:
			user_intro = Intro.objects.get(user=user)
			context = {}
			context['intro'] = user_intro
			return render(request, 'demo/viewintro.html', context)
		except:
			return render(request, 'demo/startintro.html')
	else:
		raise Http404()