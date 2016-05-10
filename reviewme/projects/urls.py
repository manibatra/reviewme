from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^dashboard/reviewer/$', views.showReviewerDash, name='reviewer_dashboard'),
	url(r'^categories/$', views.showCategories, name='categories'),
	url(r'^categories/(?P<category_id>[0-9]+)/$', views.showSubCategories, name='sub_categories'),
	url(r'^categories/subcategories/(?P<subcategory_id>[0-9]+)/$', views.showProjects, name='projects'),
	url(r'^categories/projects/(?P<project_id>[0-9]+)/$', views.projectDetail, name='project_detail'),
	url(r'^categories/projects/submit/(?P<project_id>[0-9]+)/$', views.submitProject, name='submit_project'),

]