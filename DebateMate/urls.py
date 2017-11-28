"""DebateMate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from main import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
	url(r'^signup/$', views.signup, name='signup'),
    url(r'^help/$', views.help, name='help'),
    url(r'^rules/$', views.rules, name='rules'),
    url(r'^report_argument/$', views.report_argument, name='report_argument'),
    url(r'^report_comment/$', views.report_comment, name='report_comment'),
    url(r'^view_reported_arguments/$', views.view_reported_arguments, name='view_reported_arguments'),
    url(r'^view_reported_comments/$', views.view_reported_comments, name='view_reported_comments'),
    url(r'^clear_comment_report/$',views.clear_comment_report, name='clear_comment_report'),
    url(r'^clear_argument_report/$',views.clear_argument_report, name='clear_argument_report'),
    url(r'^delete_comment/$',views.delete_comment, name='delete_comment'),
    url(r'^delete_argument/$',views.delete_argument, name='delete_argument'),
	url(r'^login/$', auth_views.login, {'template_name': 'main/login.html'}, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^join/$', views.join, name='join'),
	url(r'^set_debate/$', views.set_debate, name='set_debate'),
    url(r'^debate/$', views.debate, name='debate'),
    url(r'^spectate/$', views.spectate, name='spectate'),
    url(r'^moderate/$', views.moderate, name='moderate'),
    url(r'^confirm_comment/$', views.confirm_comment, name='confirm_comment'),
]
