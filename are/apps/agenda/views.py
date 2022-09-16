from django.shortcuts import render ,redirect,get_object_or_404
from django.views.generic import TemplateView
from agenda.models import Agenda,Conference
from speakers.models import Speaker
from agenda.forms import AgendaForm, ConferenceForm
from django.views.generic import ListView,View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.http import JsonResponse
from datetime import timedelta, date
import pandas as pd

# Create your views here.


class ConferenceCreateView(CreateView):
	model = Conference 
	fields = ['title', 'startdate','enddate']
	template_name="agenda.html"


	def get_success_url(self, **kwargs):
		return self.object.get_absolute_url()

     
class MyFormView(CreateView):
	model = Agenda 
	form_class = AgendaForm
	template_name = 'agenda.html'

	def post(self, request, *args, **kwargs):
		# objs = Conference.objects.filter(id=kwargs['pk'])[0]
		form = AgendaForm(request.POST)
		if form.is_valid():
			agenda = form.save(commit=False)
			agenda.save()
			return redirect('/agenda')


class AgendaView(ListView):
	template_name = 'agenda.html'	
	queryset = Conference.objects.all().order_by('startdate')
	
	def get_context_data(self, **kwargs):
		context = {}
		if self.queryset:
			# context = super(AgendaView, self).get_context_data(**kwargs)
			if len(self.queryset)>0:
				context['conf'] = self.queryset[0]
			else:
				context['conf'] = None
			datelist = pd.date_range(start=context['conf'].startdate,end=context['conf'].enddate)
			indexlist = [i+1 for i in range(len(datelist))]
			# context['agenda'] = Agenda.objects.all()
			agenda = Agenda.objects.all().filter(conference_id = context['conf'].id).order_by('starttime').order_by('date')

			data = {}
			for index, item in zip(indexlist, datelist):
				if agenda:
					data[str(index)] = {
						'date':item.date(),
						'data':agenda.filter(date=item.date())
					}
				else:
					data[str(index)] = {
						'date':item.date(),
						'data':[]
					}

			context['agenda'] = data
			context['speakers'] = Speaker.objects.all()
			return context
		else:
			context = {
				'conf':None,
				'agenda':{},
				'speakers': Speaker.objects.all()
			}
			return context

def edit_session_popup(request):
	session_id = request.GET.get('session_id')
	selected_session = Agenda.objects.all().filter(id=int(session_id))
	speakers = Speaker.objects.all()
	response = {
		"session":selected_session,
		"speakers":speakers
	}
	return JsonResponse(response)



