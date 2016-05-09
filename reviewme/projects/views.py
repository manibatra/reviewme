from django.shortcuts import render
from .models import Category, SubCategory, Project, Submission
from django.db.models import Count
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
	if request.user.is_authenticated():
		new_submission = Submission(project_id=project_id, student=request.user, files=request['files'], notes=request['note'])
		new_submission.save()
		response = {'status' : 1}

	else:
		response = {'status' : 0, 'msg' : 'You have to be logged in first'}


	return HttpResponse(json.dumps(response), content_type='application/json')