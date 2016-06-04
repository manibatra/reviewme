from django.conf.urls import url

from . import views

urlpatterns = [

	url(r'^begin/$', views.begin, name='begin'),
	url(r'^end/$', views.end, name='end'),

]
