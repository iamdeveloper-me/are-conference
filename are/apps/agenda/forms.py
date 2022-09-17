from django import forms
from .models import Agenda,Conference


class ConferenceForm(forms.ModelForm):
	class Meta:
		model = Conference
		fields = ['title', 'startdate', 'enddate']
		

class AgendaForm(forms.ModelForm):
	class Meta:
		model = Agenda
		fields = ['conference', 'session', 'date','starttime', 'endtime', 'duration', 'event', 'speaker']

