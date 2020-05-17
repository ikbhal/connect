from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from college.models import College

class Student(models.Model):
   name=models.CharField(max_length=500)
   mobile=models.CharField(max_length=20)
   email=models.CharField(max_length=100)
   date=models.DateTimeField(default=timezone.now)
   user = models.OneToOneField(User, on_delete=models.CASCADE,\
                               null=True, blank=True)

   def __str__(self):
       return self.name
