from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    mobile = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        #user = super(NewUserForm, self).save(commit=False)
        user = super(NewUserForm, self).save()
        #user.email = self.cleaned_data["email"]
        #user.mobile = self.cleaned_data["mobile"]
        # create student
        email = self.cleaned_data["email"]
        mobile = self.cleaned_data["mobile"]
        student = Student.objects.create(name=user.username, email=email, mobile=mobile,\
                               user=user)
        return user
