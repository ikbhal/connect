from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from django.urls import reverse

from .forms import StudentForm, NewUserForm
from admission.forms import AdmissionForm
from .models import Student
from .serializers import StudentSerializer
from admission.models import Admission
import logging

logger = logging.getLogger('student.views')

# api section begin
@api_view(['GET', 'POST', 'DELETE'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        students_serializer = StudentSerializer(students, many=True)
        return JsonResponse(students_serializer.data, safe=False)

# api section end
def index(request):
    item_list = Student.objects.order_by("-name")
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    form = StudentForm()
    page = {
            "forms" : form,
            "list": item_list,
            "title" : "Student LIST",
            }
    return render(request, 'student/index.html', page)

def detail(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        admissions = Admission.objects.filter(student__id=student_id)
        admission_form = AdmissionForm()
        admission_form.helper.form_action = reverse('admission_add',\
            args=(student_id,))
        messages.info(request, "student retrieve !!!")
    except Student.DoesNotExist:
        admissions = None
        student = None
        admission_form = None
        messages.info(request, f'student {student_id} doest not exist')
    page = {
        "student" : student,
        "admissions" : admissions,
        "admission_form" : admission_form,
        }
    return render(request, 'student/detail.html', page)

## function to remove college, it receive college item id from url ###
def remove(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    messages.info(request, "student removed !!!")
    return redirect('students')

def edit(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('student_detail',student_id=student.id)
    else:
        form = StudentForm(instance=student)
    return render(request, 'student/edit.html', {'form': form})

@login_required
def home(request):
    try:
        user = request.user
        student =  Student.objects.get(user=user)
        messages.info(request, "Student found " +  student.mobile + student.name)
    except Student.DoesNotExist:
        messsages.info("No student found for loggedn user")
        student = None
    return render(request, "student/home.html", {'student': student})

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("student_home")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "student/register.html", {'form':form})
    form = NewUserForm
    return render(request, "student/register.html", {'form': form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if  user is not None:
                login(request, user)
                return redirect("student_home")
            else:
                 messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    return render(request, 'student/login.html', {'form': form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return  redirect('login')
