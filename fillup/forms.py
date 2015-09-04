from django import forms
from fillup.models import *

class Fillup(forms.ModelForm):

	class Meta:
		model = Student
		fields = ('id_num', 'name', 'email', 'course', 'year',)