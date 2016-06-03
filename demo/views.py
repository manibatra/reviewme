from django.shortcuts import render

# Create your views here.
def begin(request):
	context = {}
	return render(request, 'demo/step1.html', context)

def middle(request):
	context = {}
	return render(request, 'demo/step2.html', context)

def end(request):
	context = {}
	return render(request, 'demo/step3.html', context)