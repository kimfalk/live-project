from django.urls import re_path

from moviegeeks import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^movie/(?P<movie_id>\d+)/$', views.detail, name='detail'),
    re_path(r'^genre/(?P<genre_id>[\w-]+)/$', views.genre, name='genre'),
    re_path(r'^search/$', views.search_for_movie, name='search_for_movie'),
]
