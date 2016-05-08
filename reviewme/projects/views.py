from django.shortcuts import render

# Create your views here.
def showCategories(request):
	return render(request, 'projects/categories.html')
