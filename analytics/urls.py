from django.urls import re_path
from analytics import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^user/(?P<user_id>\d+)/$', views.user, name='user'),
    re_path(r'^content/(?P<content_id>\d+)/$', views.content, name='content'),
    re_path(r'^cluster/(?P<cluster_id>\d+)/$', views.cluster, name='cluster'),
    re_path(r'^api/get_statistics', views.get_statistics, name='get statistics'),
	re_path(r'^api/events_on_conversions', views.events_on_conversions, name='events_on_conversions'),
    re_path(r'^api/ratings_distribution', views.ratings_distribution, name='ratings_distribution'),
	re_path(r'^api/top_content', views.top_content, name='top_content'),
    re_path(r'^api/clusters', views.clusters, name='clusters'),
    re_path(r'^lda', views.lda, name='lda'),
    re_path(r'^similarity', views.similarity_graph, name='similarity_graph'),
]