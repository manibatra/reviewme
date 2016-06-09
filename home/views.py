from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings


# Create your views here.
def landing(request):
	return render(request, "home/index.html", {'media' : settings.MEDIA_URL})
