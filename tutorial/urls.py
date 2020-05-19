from django.conf.urls import re_path
from tutorial import views

urlpatterns = [
    re_path(r'^tutorials$', views.tutorial_list),
    re_path(r'^tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    re_path(r'^tutorials/published$', views.tutorial_list_published)
]
