from django.shortcuts import render

# Create your views here.

def aboutPage(request):
	return render(request, 'info/about.html')

def privacyPage(request):
	return render(request, 'info/privacy.html')
