from django.forms import ModelForm
from .models import Inquiry

class NameForm(ModelForm):
	class Meta:
		model = Inquiry
		fields = '__all__'