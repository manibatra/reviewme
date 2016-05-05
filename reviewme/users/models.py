from __future__ import unicode_literals

from django.db import models
from django.conf import settings
import uuid


#model to save the user verification code
# Create your models here.
class UserVerification(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	ver_code = models.CharField(max_length=32)