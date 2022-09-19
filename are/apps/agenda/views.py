from django.shortcuts import render ,redirect,get_object_or_404
from django.views.generic import TemplateView
from agenda.models import Agenda,Conference
from speakers.models import Speaker
from agenda.forms import AgendaForm, ConferenceForm
from django.views.generic import ListView,View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
<<<<<<< HEAD
from django.utils.timezone import now
from django.http import JsonResponse
from datetime import timedelta, date
import pandas as pd
from speakers.models import Speaker


class ConferenceCreateView(CreateView):
	model = Conference 
	form_class = ConferenceForm
=======
# Create your views here.


class ConferenceCreateView(CreateView):
	# import pdb;pdb.set_trace()
	model = Conference 
	fields = ['title', 'startdate','enddate']
>>>>>>> f340b38 (agenda list show)


class ConferenceListView(ListView):
    model = Conference
    temlate_name = 'agenda.html'

class AgendaCreateView(CreateView):
	# import pdb;pdb.set_trace()
	model = Agenda 
	fields = ['session', 'starttime','endtime','duration','event']


class AgendaListView(ListView):
    model = Agenda
    temlate_name = 'agenda.html'

     
class MyFormView(CreateView):
	model = Agenda 
	form_class = AgendaForm
	template_name = 'agenda.html'
	# success_url = reverse('agenda:agenda_list')

	def post(self, request, *args, **kwargs):
		# objs = Conference.objects.filter(id=kwargs['pk'])[0]
		form = AgendaForm(request.POST)
		if form.is_valid():
			agenda = form.save(commit=False)
			agenda.save()
			return redirect('/agenda')


<<<<<<< HEAD
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
=======


# class ConferenceView(ListView):
# 	form_class = AgendaForm
# 	template_name = 'agenda.html'
# 	# success_url = reverse_lazy('agenda:agenda')


# class ConferenceCreateView(CreateView):
# 	model = Conference
# 	form_class = ConferenceForm

# 	def get_success_url(self, **kwargs):
# 		return self.object.get_absolute_url()




# class AgendaView(ListView):
# 	model = Agenda
# 	template_name = 'agenda.html'
# 	# import pdb; pdb.set_trace()
# 	# queryset = Agenda.objects.all()
	
# 	def get_context_data(self, **kwargs):
# 		# import pdb; pdb.set_trace()
# 		context = super().get_context_data(**kwargs)
# 		context['reports_list'] = Agenda.objects.all().order_by('id')
# 		return context
# 	def get_queryset(self):
# 		import pdb; pdb.set_trace()
# 		return Agenda.objects.all().order_by('id')

# 	def get_context_data(self, **kwargs):
# 		import pdb; pdb.set_trace()
# 		context = super().get_context_data(**kwargs)
# 		context = Agenda.objects.all().order_by('id')
# 		return {'context':context}
>>>>>>> f340b38 (agenda list show)

			context['agenda'] = data

<<<<<<< HEAD
			context['all_speakers'] = Speaker.objects.all()

			return context
		else:
			context = {
				'conf':None,
				'agenda':{},
				'speakers': Speaker.objects.all()
			}

			context['all_speakers'] = Speaker.objects.all()
			return context
=======
# def AddAgenda(request):
# 	if request.method == 'POST' :
# 		# import pdb;pdb.set_trace()
# 		session = request.POST.get("session")
# 		starttime = request.POST.get("starttime")
# 		endtime = request.POST.get("endtime")
# 		duration = request.POST.get("duration")
# 		event = request.POST.get("event")
# 		agenda_register = Agenda(session=session,starttime=starttime,endtime=endtime,duration=duration,event=event)
# 		agenda_register.save()

# 	return redirect("agenda:agenda_list")

	# def get_success_url(self, **kwargs):
	# 	return self.object.get_absolute_url()
>>>>>>> f340b38 (agenda list show)

def edit_session_popup(request):
	session_id = request.GET.get('session_id')
	selected_session = Agenda.objects.all().filter(id=int(session_id))
	speakers = Speaker.objects.all()
	response = {
		"session":selected_session,
		"speakers":speakers
	}
	return JsonResponse(response)





