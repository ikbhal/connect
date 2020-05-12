from django.db import models
from django.utils import timezone
from college.models import College
from student.models import Student
from datetime import date

class Admission(models.Model):
    # on delete should not delete student
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    # on delete should not delete college
    college=models.ForeignKey(College, on_delete=models.CASCADE)
    # only year is enough, some time month is needed
    start_date = models.DateField(default=date.today())
    # end date year is enough, some course need month
    end_date = models.DateField(default=date.today())

    date=models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.student.name if self.student else 'No Student'} {self.college.name} \
                {self.start_date.year} - {self.end_date.year}"
