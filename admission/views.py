from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import date
import datetime
from .models import Admission
from .forms import AdmissionForm
from student.models import Student
from college.models import College
from django.contrib import messages
# Create your views here.

def delete(request, student_id, admission_id):
    try:
        admission = Admission.objects.get(id=admission_id)
        admission.delete()
        messages.info(request, "admission removed !!!")
    except Admission.DoesNotExist:
        messages.info(request, f'Invalid Admission id {admission_id}')

    return redirect('student_detail', student_id=student_id)

def add(request, student_id):
    # we might need form for admission
    # collect student id from request.POST
    # get collwege id from request.POST
    # get start date , end date for admission from request.POST
    # get student
    # get college
    # create admission object

    # for simplicity, we assume, all details in request.POST
    form = AdmissionForm(request.POST)
    if form.is_valid():
         form.save()

    return redirect('student_detail', student_id=student_id)

def edit(request, student_id, admission_id):
    try:
        student = Student.objects.get(id=student_id)
        admission = Admission.objects.get(id=admission_id)
        if request.method == "POST":
            admission_form = AdmissionForm(request.POST, instance=admission)
            admission_form.save()
            return redirect('student_detail', student_id)
        else:
             admission_form =  AdmissionForm(instance=admission)
    except Admission.DoesNotExist:
        messages.error(request, f"admission {admission_id} does not exist")
        admission = None
        student = None
    return render(request, 'admission/edit.html', \
                  {'student': student, 'admission':admission, \
                   'admission_form' : admission_form})
