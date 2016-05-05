from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	url(r'^signup/$', views.signupUser, name='signup_user'),
	url(r'^login/$', views.loginUser, name='login_user'),
	url(r'^logout/$', views.logout_user, name='logout_user'),
	url(r'^verification-start/$', views.verification_start, name='verification_start'),
	url(r'^verification-confirm/(?P<uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})(?P<ver_code>[0-9a-zA-Z]{32})/$'
					, views.verification_confirm, name='verification_confirm'),
	url(r'^verification-complete/$', views.verification_complete, name='verification_complete'),
	url(r'^reset-password/$', auth_views.password_reset, {'template_name': 'users/password_reset_start.html'}, name='password_reset_start'),
	url(r'^reset-password-done/$', auth_views.password_reset_done, {'template_name': 'users/password_reset_done.html'}, name="password_reset_done"),



]