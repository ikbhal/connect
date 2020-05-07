from django.db import models
from django.utils import timezone

class College(models.Model):
   name=models.CharField(max_length=500)
   city=models.CharField(max_length=100)
   state=models.CharField(max_length=50)
   date=models.DateTimeField(default=timezone.now)

   def __str__(self):
       return self.name
