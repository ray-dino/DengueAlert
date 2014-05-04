from django.conf.urls import patterns, include, url
from django.contrib import admin

from denguealert import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'},
        name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url': '/login/'},
        name='logout'),

    url(r'^report/$', views.ReportView.as_view(), name='report'),
)
