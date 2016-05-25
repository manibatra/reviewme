from django.shortcuts import render
from django.http import HttpResponse

def custom_404_view(request):
	return render(request, "message.html", {'heading' : 'HTTP 404 ERROR', 'message' : 'Oops! The page you are trying to view does not exist!'})

def custom_500_view(request):
	return render(request, "message.html", {'heading' : 'HTTP 500 ERROR', 'message' : 'Oops! Something broke at our end! We are "Reviewing" it ASAP!!!'})

def letsencrypt(request, id):
	return HttpResponse("ey75qXa81d3mMXDqG7oHH2zR-U7je4JDGvnSZxNYfqw.aG1MGpsjuniwg0DZThLFdS7HIWqEwsAGBXppIBQBLNQ", content_type='text/plain')