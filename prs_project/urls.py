"""prs_project URL Configuration"""
from django.urls import include, re_path
from django.contrib import admin
from moviegeeks import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^movies/', include('moviegeeks.urls')),
    re_path(r'^collect/', include('collector.urls')),
    re_path(r'^analytics/', include('analytics.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^rec/', include('recommender.urls'))
]

