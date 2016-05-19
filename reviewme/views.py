from django.shortcuts import render

def custom_404_view(request):
	return render(request, "message.html", {'heading' : 'HTTP 404 ERROR', 'message' : 'Oops! The page you are trying to view does not exist!'})

def custom_500_view(request):
	return render(request, "message.html", {'heading' : 'HTTP 500 ERROR', 'message' : 'Oops! Something broke at our end! We are "Reviewing" it ASAP!!!'})