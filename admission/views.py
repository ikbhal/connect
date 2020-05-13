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
    """
    try :
        student_id = request.POST['student_id']
        college_id = request.POST['college_id']
        format_str="%Y-%m-%d"
        #time data '2001-06-01' does not match format '%m/%d/%Y'
        start_date = request.POST['start_date']
        start_date = datetime.datetime.strptime(start_date, format_str).date()
        end_date = request.POST['end_date']
        end_date = datetime.datetime.strptime(end_date, format_str).date()
        date = timezone.now()

        student = Student.objects.get(id=student_id)
        college = College.objects.get(id=college_id)
        admission = Admission()
        admission.student = student
        admission.college = college
        admission.start_date = start_date
        admission.end_date = end_date
        admission.date = date

        admission.save()
    except Student.DoesNotExist:
        messages.error(request, "student_id is wrong")
    except College.DoesNotExist:
        messages.error(request, "college_id is wrong")

    return redirect('student_detail', student_id=student_id)
    """
