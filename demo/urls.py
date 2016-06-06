from django.conf.urls import url

from . import views

urlpatterns = [

	url(r'^begin/$', views.begin, name='begin'),

]
