from django.urls import re_path
from collector import views

urlpatterns = [
    re_path(r'^log/$', views.log, name='log'),
]


