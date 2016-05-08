from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Role(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	student = models.BooleanField()
	reviewer = models.BooleanField()

class Category(models.Model):
	name = models.CharField(max_length=132)
	description = models.TextField()


class SubCategory(models.Model):
	name = models.CharField(max_length=132)
	description = models.TextField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Project(models.Model):
	name = models.CharField(max_length=132)
	description = models.TextField()
	sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)


class Submission(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	student = models.ForeignKey(User, on_delete=models.CASCADE)
	submitted_on = models.DateTimeField(auto_now_add=True)
	returned_on = models.DateTimeField()
	cost = models.IntegerField()
	finished = models.BooleanField(default=False)


def review_directory_path(instance, filename):
		# file will be uploaded to MEDIA_ROOT/<userid>_review_<id>
		return '{1}_review_{0}'.format(instance.id, instance.project.user)

class Review(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
	assined_time = models.DateTimeField()
	finished_time = models.DateTimeField()
	notes = models.TextField()
	feedback = models.TextField()
	files = models.FileField(upload_to=review_directory_path)



