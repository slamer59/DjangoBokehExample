"""DjangoBokehExample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from bokehplot.views import simple_chart, get_json, stocks
from happiness.views import IndividualDashboardView, TeamDashboardView, AddHappinessView, HomeView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^simple_chart/$', simple_chart, name="simple_chart"),
    url(r'^get_json/$', get_json, name="get_json"),
    url(r'^stocks/$', stocks, name="stocks"),
    url(r'^(?P<pk>[0-9]+)/individual/', IndividualDashboardView.as_view(), name='individual'),
    url(r'^(?P<pk>[0-9]+)/team/', TeamDashboardView.as_view(), name='team'),
    url(r'^(?P<pk>[0-9]+)/add_happiness/', AddHappinessView.as_view(), name='add_happiness'),
    url(r'^$', HomeView.as_view(), name='home'),
]
