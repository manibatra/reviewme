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




urlpatterns = [
	url(r'^', include('home.urls', namespace="home")),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', global_views.login_view, name='login'),
    url(r'^users/', include('users.urls', namespace="users")),
    url(r'^projects/',include('projects.urls', namespace="projects")),
    url(r'^users/reset-password-done/$', auth_views.password_reset_done, {'template_name': 'users/password_reset_done.html'}, name="password_reset_done"),
     url(r'^password/reset-password-confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm, {'template_name': 'users/password_reset_confirm.html'}, name="password_reset_confirm"),
    url(r'^password/reset-password-complete/$', auth_views.password_reset_complete, {'template_name': 'users/password_reset_complete.html'}, name="password_reset_complete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
