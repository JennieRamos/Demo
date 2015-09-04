from django.shortcuts import render
from models import *
from forms import *

# Create your views here.

def fillup(request):
	if request.method == "POST":
		form = forms.Fillup(request.POST)

		if form.is_valid():
			form.save()
	else:
		form = forms.Fillup()
	return render(request, 'fillup.html', {'form': form})
