from django import forms
from .models import Agenda,Conference

class ConferenceForm(forms.ModelForm):
	class Meta:
		model = Conference
		fields = ['title', 'startdate', 'enddate']
		

class AgendaForm(forms.ModelForm):
	class Meta:
		model = Agenda
		fields = ['session', 'starttime', 'endtime', 'duration', 'event']

