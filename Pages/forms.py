from django import forms
from Inquiry.models import Inquiry

class NameForm(forms.Form):
	name = forms.CharField(label='Name', max_length=30)
	phone = forms.CharField(label='phone', max_length=12)
	reason = forms.CharField(label='body', max_length=300)