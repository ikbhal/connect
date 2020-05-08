from django.shortcuts import render,redirect
from django.contrib import messages

from .forms import CollegeForm
from .models import College

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
    college = College.objects.get(id=college_id)
    messages.info(request, "college retrieved !!!")
    page = { 
            "college" : college,
            }
    return render(request, 'college/detail.html', page)


### function to remove college, it receive college item id from url ###
def remove(request, college_id):
    college = College.objects.get(id=college_id)
    college.delete()
    messages.info(request, "college removed !!!")
    return redirect('college')

