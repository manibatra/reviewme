from django.conf.urls import url

from . import views

urlpatterns = [

	url(r'^about/$', views.aboutPage, name='about'),
	url(r'^privacy/$', views.privacyPage, name='privacy'),

]
