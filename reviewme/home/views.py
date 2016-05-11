from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def landing(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse("projects:categories"))
	else:
		return render(request, "home/index.html")
