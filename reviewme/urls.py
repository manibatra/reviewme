"""reviewme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views as global_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from home import views




urlpatterns = [
	url(r'^', include('home.urls', namespace="home")),
    url(r'^.well-known/acme-challenge/(?P<id>.*)$', global_views.letsencrypt),
    url(r'^{}/admin/'.format(settings.ADMIN_URL_PATH), admin.site.urls),
    url(r'^users/', include('users.urls', namespace="users")),
    url(r'^demo/', include('demo.urls', namespace="demo")),
    url(r'^content/',include('projects.urls', namespace="projects")),
    url(r'^info/',include('info.urls', namespace="info")),
    url(r'^users/reset-password-done/$', auth_views.password_reset_done, {'template_name': 'users/password_reset_done.html'}, name="password_reset_done"),
    url(r'^password/reset-password-confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm, {'template_name': 'users/password_reset_confirm.html'}, name="password_reset_confirm"),
    url(r'^password/reset-password-complete/$', auth_views.password_reset_complete, {'template_name': 'users/password_reset_complete.html'}, name="password_reset_complete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'reviewme.views.custom_404_view'
handler500 = 'reviewme.views.custom_500_view'