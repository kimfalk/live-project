from django.urls import re_path

from recommender import views

urlpatterns = [
    re_path(r'^chart/', views.chart, name='chart'),
    re_path(r'^association_rule/(?P<content_id>\w+)/$',
        views.get_association_rules_for,
        name='get_association_rules_for'),
    re_path(r'^ar/(?P<user_id>\w+)/$',
        views.recs_using_association_rules,
        name='recs_using_association_rules'),
    re_path(r'^sim/user/(?P<user_id>\w+)/(?P<sim_method>\w+)/$',
        views.similar_users, name='similar_users'),
    re_path(r'^cb/item/(?P<content_id>\w+)/$',
        views.similar_content, name='similar_content'),
    re_path(r'^cb/user/(?P<user_id>\w+)/$',
        views.recs_cb, name='recs_cb'),
    re_path(r'^cf/user/(?P<user_id>\w+)/$',
        views.recs_cf, name='recs_cb'),
    re_path(r'^funk/user/(?P<user_id>\w+)/$',
        views.recs_funksvd, name='recs_funksvd'),
    re_path(r'^fwls/user/(?P<user_id>\w+)/$',
        views.recs_fwls, name='recs_fwls'),
    re_path(r'^nnmf/user/(?P<user_id>\w+)/$',
        views.recs_nnmf, name='recs_nnmf'),
    re_path(r'^bpr/user/(?P<user_id>\w+)/$',
        views.recs_bpr, name='recs_fwls'),
    re_path(r'^pop/user/(?P<user_id>\w+)/$',
        views.recs_pop, name='recs_pop')
]
