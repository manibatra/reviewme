from django.shortcuts import render
from .models import Category, SubCategory
from django.db.models import Count

# Create your views here.
def showCategories(request):
	context = {}
	all_categories = Category.objects.annotate(num_projects=Count('subcategory__project', distinct=True))
	context['items'] = all_categories
	return render(request, 'projects/categories.html', context)

def showSubCategories(request, category_id):
	context = {}
	all_sub_categories = SubCategory.objects.filter(category=category_id).annotate(num_projects=Count('project', distinct=True))
	context['items'] = all_sub_categories
	return render(request, 'projects/categories.html', context)