from django import forms
from .models import Speaker

class SpeakerForm(forms.ModelForm):
	class Meta:
		model = Speaker
		fields = ['name','profile_image','designation','detail']
