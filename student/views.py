from django.shortcuts import render,redirect
from django.contrib import messages

from .forms import StudentForm
from .models import Student
from admission.models import Admission

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
    student = Student.objects.get(id=student_id)
    admissions = Admission.objects.filter(student__id=student_id)
    messages.info(request, "student retrieve !!!")
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

