from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


def review_directory_path(instance, filename):
		# file will be uploaded to MEDIA_ROOT/<userid>_review_<id>
		return 'intros/{0}/intro_review.zip'.format(instance.user.id)


# Create your models here.
class Intro(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	q_a = models.TextField()
	q_b = models.TextField()
	review_files = models.FileField(upload_to=review_directory_path, blank=True, null=True)

	def __unicode__(self):
		return self.user.get_username()
