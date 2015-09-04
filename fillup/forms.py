from django import forms
from fillup.models import *

class Fillup(forms.ModelForm):
    id_num = models.CharField(label= "ID No.", max_length=10)
    name = models.CharField(label= "Name", max_length=40)
    email = models.CharField(label= "Email", max_length=40)
    course = models.TextField(label= "Course")
    year = models.TextField(label= "Year")

    class Meta:
	    model = Student
	    fields = ('id_num', 'name', 'email', 'course', 'year',)