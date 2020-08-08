from django.shortcuts import render
from django.http import HttpResponseRedirect
from Inquiry.forms import NameForm

# Create your views here.
def home_view(request):
	flag = False
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
		else:
			flag = form.errors
	else:
		form = NameForm
	context = {
		'form': form,
		'stuff':request.method,
		'flag':flag
	}
	return render(request, 'index.html', context)

def submitted_view(request):
	return render(request, 'submitted.html')

def coming_soon_view(request):
	return render(request, 'coming_soon.html')