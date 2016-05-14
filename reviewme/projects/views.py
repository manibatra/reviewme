from django.shortcuts import render
from .models import Category, SubCategory, Project, Submission, Reviewer, Role
from django.db.models import Count
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
import datetime
from datetime import timedelta
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
				new_submission.submitted_files = request.FILES['projectzip']
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
	if request.user.is_authenticated():


		current_reviewer = User.objects.get(pk=request.user.id)

		#did the user applied to be a reivewer
		current_role = Role.objects.get(user=current_reviewer)

		if current_role.reviewer:
			#list all the availablel projects that the reviewer is eligible to review
			all_eligible_projects = Reviewer.objects.filter(user=current_reviewer).filter(training_complete=True).values_list('project__id', flat=True)
			projects_available = Submission.objects.filter(project__in=all_eligible_projects).filter(reviewer__isnull=True).filter(returned_on__isnull=
				True).values('project__name', 'project__id', 'project__cost').annotate(count=Count('project'))

			context = {}
			context['available'] = projects_available

			#list all the submissions available to review

			#fist check if submission has been sitting for more than time limit
			#setting timedelta as 5 for a time cap of 4 hrs to review
			lapsed_submissions = Submission.objects.filter(finished=False).filter(reviewer=current_reviewer).filter(assigned_time__lt=
									(datetime.datetime.utcnow().replace(tzinfo=utc))-timedelta(hours=3, minutes=59))
			for submission in lapsed_submissions:
				submission.reviewer = None
				submission.assigned_time = None
				submission.save()


			#list all the submissions still eligible
			projects_assigned = Submission.objects.filter(reviewer=current_reviewer).values('project__name', 'id', 'assigned_time',
								'project__cost').filter(returned_on__isnull=True)
			for dictionary in projects_assigned:
				time_left = time_remaining(dictionary['assigned_time'])
				dictionary['time_remaining'] = time_left

			context['assigned'] = projects_assigned
			return render(request, 'projects/reviewerdash.html', context)
		else:
			context = {}
			context['heading'] = "Become a reviewer"
			context['message'] = "You have not yet applied to be a reviewer. You can do so by clicking the button below."
			context['button'] = True
			context['button_message'] = "Apply"
			context['button_url'] = "/content/categories"
			return render(request, 'message.html', context)
	else:
		raise HttpResponseRedirect(reverse('users:login'))

def time_remaining(assigned_time):
	dt = datetime.datetime.utcnow().replace(tzinfo=utc)  - assigned_time
	hours = dt.seconds/60/60
	return 4 - hours


def assignSubmission(request):
	if request.method == 'POST':
		if request.user.is_authenticated():
			current_reviewer = User.objects.get(pk=request.user.id)
			#checking if two submissions have been assigned to the reivewer and not finished
			currently_assigned = Submission.objects.filter(reviewer=current_reviewer).filter(returned_on__isnull=True)
			if len(currently_assigned) >= 2:
				messages.add_message(request, messages.ERROR, 'Assignment limit reached')
				return HttpResponseRedirect(reverse('projects:reviewer_dashboard'))
			else:
				#less than two submissions assigned, assign the project
				current_submissions = Submission.objects.filter(project__id=request.POST['project_id']).filter(reviewer__isnull=True).order_by('submitted_on')
				submission_to_assign = current_submissions[0]
				submission_to_assign.assigned_time = datetime.datetime.utcnow().replace(tzinfo=utc)
				submission_to_assign.reviewer = current_reviewer
				submission_to_assign.save()
				messages.add_message(request, messages.SUCCESS, 'You have been assigned the submission')
				return HttpResponseRedirect(reverse('projects:reviewer_dashboard'))
		else:
			return HttpResponseRedirect(reverse('users:login'))

	else:
		raise Http404()

#method to show the submission page to the reviewer
def showSubmission(request, submission_id):

	if request.user.is_authenticated():
		current_user = User.objects.get(pk=request.user.id)
		current_user_role = Role.objects.get(user=current_user)
		if current_user_role.reviewer:
			current_submission = Submission.objects.get(id=submission_id, reviewer=current_user);
			context = {}
			context['submission'] = current_submission
			return render(request, 'projects/submission.html', context)
		else:
			raise Http404()
	else:
		raise Http404()


#method to submit review
def submitReview(request, submission_id):
	if request.method == 'POST':
		if request.user.is_authenticated():
			current_submission = Submission.objects.get(pk=submission_id)
			try:
				current_submission.review_files = request.FILES['projectzip']
			except:
				messages.add_message(request, messages.ERROR, 'Oops you did not submit any file')
				return HttpResponseRedirect('/content/submission/' + submission_id)
			current_submission.feedback = request.POST['feedback']
			if 'finished' in request.POST:
				current_submission.finished = True
			else:
				current_submission.finished = False #get the value from post
			current_submission.returned_on = datetime.datetime.utcnow().replace(tzinfo=utc)
			current_submission.save()
			messages.add_message(request, messages.SUCCESS, 'Your review has been submitted.')
			return HttpResponseRedirect(reverse('projects:reviewer_dashboard'))
		else:
			messages.add_message(request, messages.ERROR, 'You have to be logged in to submit a review.')
			return HttpResponseRedirect(reverse('projects:reviewer_dashboard'))
	raise Http404()


#method to show the student dashboard
def showStudentDash(request):
	if request.user.is_authenticated():
		context = {}
		return render(request, "projects/studentdash.html", context)
	else:
		return HttpResponseRedirect(reverse('users:login'))
