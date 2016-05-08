from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^categories/$', views.showCategories, name='categories'),
	url(r'^categories/(?P<category_id>[0-9]+)/$', views.showSubCategories, name='sub_categories'),
	url(r'^categories/subcategories/(?P<subcategory_id>[0-9]+)/$', views.showProjects, name='projects'),

]