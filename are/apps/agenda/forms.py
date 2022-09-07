from django import forms
from .models import Agenda,Conferense


class ConferenseForm(forms.ModelForm):
	class Meta:
		model = Conferense
		fields = ['title', 'startdate', 'enddate']

class AgendaForm(forms.ModelForm):
	class Meta:
		model = Agenda
		fields = ['session', 'starttime', 'endtime', 'duration', 'event']

