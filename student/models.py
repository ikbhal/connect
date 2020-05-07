from django.db import models
from django.utils import timezone
from college.models import College

class Student(models.Model):
   name=models.CharField(max_length=500)
   mobile=models.CharField(max_length=20)
   email=models.CharField(max_length=100)
   date=models.DateTimeField(default=timezone.now)
   college = models.ForeignKey(College, on_delete=models.CASCADE)

   def __str__(self):
       return self.name