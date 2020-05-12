from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages

from .forms import StudentForm
from .models import Student
from admission.models import Admission
import logging

logger = logging.getLogger('student.views')

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
        logger.debug("admissions ikb", admissions)
        messages.info(request, "student retrieve !!!")
    except Student.DoesNotExist:
        admissions = None
        student = None
        messages.info(request, f'student {student_id} doest not exist')
    page = {
        "student" : student,
        "admissions" : admissions,
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
