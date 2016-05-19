from __future__ import unicode_literals

from django.db import models
from django.conf import settings
import uuid
from django.contrib.auth.models import User



#model to save the user verification code
# Create your models here.
class UserVerification(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	ver_code = models.CharField(max_length=32)

class UserName(User):
	class Meta:
		proxy = True

	def __unicode__(self):
		return self.get_full_name()