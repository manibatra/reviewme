from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Role(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	student = models.BooleanField()
	reviewer = models.BooleanField()

	def __unicode__(self):
		return self.user.get_username()

class Category(models.Model):
	name = models.CharField(max_length=132)
	description = models.TextField()

	def __unicode__(self):
		return self.name

class SubCategory(models.Model):
	name = models.CharField(max_length=132)
	description = models.TextField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.name + "  (" + self.category.name + ")"

class Project(models.Model):
	name = models.CharField(max_length=132)
	description = models.TextField()
	sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
	cost = models.IntegerField()

	def __unicode__(self):
		return self.name + "  (" + self.sub_category.name + ")    -     " + str(self.cost)

class Reviewer(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	training_complete = models.BooleanField(default=False)
	project = models.ForeignKey(Project, on_delete=models.CASCADE)


	def __unicode__(self):
		return self.user.get_username() + "    -    " + self.project.name


def review_directory_path(instance, filename):
		# file will be uploaded to MEDIA_ROOT/<userid>_review_<id>
		return '{1}_submission_{0}'.format(instance.project.name, instance.student)


class Submission(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	student = models.ForeignKey(User, on_delete=models.CASCADE)
	reviewer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="reviewed_by")
	submitted_on = models.DateTimeField(auto_now_add=True)
	returned_on = models.DateTimeField(null=True, blank=True)
	finished = models.BooleanField(default=False)
	assigned_time = models.DateTimeField(null=True, blank=True)
	finished_time = models.DateTimeField(null=True, blank=True)
	notes = models.TextField(null=True, blank=True)
	feedback = models.TextField(null=True, blank=True)
	files = models.FileField(upload_to=review_directory_path)


	def __unicode__(self):
		if self.reviewer:
			return self.student.get_username() + "  -  " + self.project.name +  "  -   " + self.reviewer.get_username()
		else:
			return self.student.get_username() + "  -  " + self.project.name







