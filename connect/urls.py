"""connect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from college import views
from student import views as student_views
from admission import views as admission_views

urlpatterns = [
    path('tut/api/', include('tutorial.urls')),
    path('api/', include('student.urls')),
    path('', views.index, name='home'),
    path('home', student_views.home, name="student_home"),
    path('register', student_views.register, name="register"),
    path('login', student_views.login_request, name="login"),
    path('logout', student_views.logout_request,  name="logout"),
    path('colleges', views.index, name='college'),
    path('colleges/<int:college_id>', views.detail, name='college_detail'),
    path('colleges/<int:college_id>/edit', views.edit, name='college_edit'),
    path('delcollege/<int:college_id>', views.remove, name='remove'),
    path('students', student_views.index, name='students'),
    path('students/<int:student_id>', student_views.detail,\
         name='student_detail'),
    path('students/<int:student_id>/edit', student_views.edit,\
         name='student_edit'),
    path('students/<int:student_id>/admissions/<int:admission_id>',\
         admission_views.delete, \
         name='admission_delete'),
    path('students/<int:student_id>/admissions', \
         admission_views.add, name='admission_add'),
    path('students/<int:student_id>/admissions/<int:admission_id>/edit', \
         admission_views.edit, name='admission_edit'),

    path('admin/', admin.site.urls),
]
