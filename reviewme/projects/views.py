from django.shortcuts import render
from .models import Category, SubCategory, Project, Submission, Reviewer
from django.db.models import Count
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
import datetime
from django.utils.timezone import utc
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
	if request.user.is_authenticated:
		current_reviewer = User.objects.get(pk=request.user.id)
		all_eligible_projects = Reviewer.objects.filter(user=current_reviewer).filter(training_complete=True).values_list('project__id', flat=True)
		projects_available = Submission.objects.filter(project__in=all_eligible_projects).filter(reviewer__isnull=True).filter(returned_on__isnull=
			True).values('project__name', 'project__id', 'project__cost').annotate(count=Count('project'))

		context = {}
		context['available'] = projects_available
		projects_assigned = Submission.objects.filter(reviewer=current_reviewer).values('project__name', 'id', 'assigned_time')
		for dictionary in projects_assigned:
			dictionary['time_remaining'] = time_remaining(dictionary['assigned_time'])

		context['assigned'] = projects_assigned
		return render(request, 'projects/reviewerdash.html', context)
	else:
		raise Http404()

def time_remaining(assigned_time):
	dt = datetime.datetime.utcnow().replace(tzinfo=utc)  - assigned_time
	hours = dt.seconds/60/60
	return 2 - hours


def assignSubmission(request, submission_id):
	if request.method == 'POST':
		if request.user.is_authenticated:
			current_reviewer = User.objects.get(pk=request.user.id)
			currently_assigned = Submission.objects.filter(reviewer=current_reviewer)
			if len(currently_assigned) >= 2:
				messages.add_message(request, messages.ERROR, 'Assignment limit reached')
				return HttpResponseRedirect(reverse('projects:reviewer_dahsboard'))
			else:
				current_submission = Submission.objects.get(pk=submission_id)
				currently_submission.assigned_time = datetime.datetime.utcnow().replace(tzinfo=utc)
				current_submission.reviewer = current_reviewer
				messages.add_message(request, messages.SUCCESS, 'You have been assigned the submission')
				return HttpResponseRedirect(reverse('projects:reviewer_dahsboard'))
		else:
			return HttpResponseRedirect(reverse('users:login'))

	else:
		raise Http404()
