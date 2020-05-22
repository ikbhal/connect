from django.conf.urls import re_path
from student import views

urlpatterns = [
    re_path(r'^students', views.student_list_add_delete),
]
