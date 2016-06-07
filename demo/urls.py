from django.conf.urls import url

from . import views

urlpatterns = [

	url(r'^begin/$', views.begin, name='begin'),
	url(r'^intro/start/$', views.start_intro, name='start_intro'),
	url(r'^intro/submit/$', views.submit_intro, name='submit_intro'),
	url(r'^intro/view/$', views.view_intro, name='view_intro'),
	url(r'^intro/rubric/$', views.view_rubric, name='view_rubric'),

]
