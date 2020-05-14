from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages

from .forms import CollegeForm
from .models import College
from admission.models import Admission

import logging

logger = logging.getLogger(__name__)

def index(request):
    item_list = College.objects.order_by("-name")
    if request.method == "POST":
        form = CollegeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('college')
    form = CollegeForm()
    page = {
            "forms" : form,
            "list": item_list,
            "title" : "College LIST",
            }
    return render(request, 'college/index.html', page)

def detail(request, college_id):
    try:
        college = College.objects.get(id=college_id)
        admissions = Admission.objects.filter(college__id=college_id)
        logger.debug("admissions", admissions)
        messages.info(request, "college retrieve !!!")
    except College.DoesNotExist:
        college = None
        admissions = None
        messages.error(request, f'College {college_id} doest not exist')
    except Admissions.DoesNotExist:
        admissions = None
        messages.info(request, "no students exist")

    page = {
        "college" : college,
        "admissions" : admissions,
        }
    return render(request, 'college/detail.html', page)


### function to remove college, it receive college item id from url ###
def remove(request, college_id):
    college = College.objects.get(id=college_id)
    college.delete()
    messages.info(request, "college removed !!!")
    return redirect('college')

def edit(request, college_id):
    college = get_object_or_404(College, pk=college_id) # T import get_objct..
    if request.method == "POST":
        form = CollegeForm(request.POST, instance=college) # T CollegeForm crete if not
        if form.is_valid():
            college = form.save(commit=False)
            college.save()
            redirect('college_detail', college_id=college_id) #  T C url exist
    else:
        form = CollegeForm(instance=college)
    return  render(request, 'college/edit.html', {'form': form}) # T edit.html

