from django.shortcuts import render
from .models import Category, SubCategory, Project, Submission
from django.db.models import Count
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.contrib import messages


import json

# Create your views here.
def showCategories(request):
	context = {}
	all_categories = Category.objects.annotate(num_projects=Count('subcategory__project', distinct=True))
	context['type'] = 'categories'
	context['items'] = all_categories
	return render(request, 'projects/categories.html', context)

def showSubCategories(request, category_id):
	context = {}
	all_sub_categories = SubCategory.objects.filter(category=category_id).annotate(num_projects=Count('project', distinct=True))
	context['type'] = 'subcategories'
	context['items'] = all_sub_categories
	return render(request, 'projects/categories.html', context)

def showProjects(request, subcategory_id):
	context = {}
	all_projects = Project.objects.filter(sub_category=subcategory_id)
	context['type'] = 'projects'
	context['items'] = all_projects
	return render(request, 'projects/categories.html', context)


def projectDetail(request, project_id):
	context = {}
	current_project = Project.objects.get(pk=project_id)
	context['project'] = current_project
	return render(request, 'projects/projectdetail.html', context)


def submitProject(request, project_id):
	if request.method == 'POST':
		if request.user.is_authenticated():
			project = Project.objects.get(pk=project_id)
			user = User.objects.get(pk=request.user.id)
			new_submission = Submission(project=project, student=user, notes=request.POST['note'])
			try:
				new_submission.files = request.FILES['projectzip']
			except:
				messages.add_message(request, messages.ERROR, 'Oops you did not submit any file')
				return HttpResponseRedirect('/content/categories/projects/' + project_id)

			new_submission.save()
			messages.add_message(request, messages.SUCCESS, 'Your project has been submitted for review')
			return HttpResponseRedirect(reverse('projects:categories'))

		else:
			messages.add_message(request, messages.ERROR, 'You have to be logged in to submit a project.')
			return HttpResponseRedirect('/content/categories/projects/' + project_id)

		return HttpResponse(json.dumps(response), content_type='application/json')

def showReviewerDash(request):
	return render(request, 'projects/reviewerdash.html')