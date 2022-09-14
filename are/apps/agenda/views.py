from django.shortcuts import render ,redirect,get_object_or_404
from django.views.generic import TemplateView
from agenda.models import Agenda,Conference
from agenda.forms import AgendaForm, ConferenceForm
from django.views.generic import ListView,View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.timezone import now
from datetime import timedelta, date

# Create your views here.


class ConferenceCreateView(CreateView):
	model = Conference 
	fields = ['title', 'startdate','enddate']
	template_name="agenda.html"
	

	def get_success_url(self, **kwargs):
		return self.object.get_absolute_url()

class AgendaCreateView(CreateView):
	# import pdb; pdb.set_trace()
	model = Agenda 
	form_class = AgendaForm
	template_name = 'agenda.html'
	new_agenda = None

	def form_valid(self, form):
	    conference = self.get_object()
	    form.instance.conference = conference
	    return super().form_valid(form)
	
	# def agenda_new(request,pk):
	# 	obj = Conference.objects.filter(id=kwargs['pk'])[0]
	# 	date_range = Agenda.objects.filter(date_range("conf.startdate","conf.enddate"))		       
	# 	if request.method == 'POST':
	# 		form = AgendaForm(request.POST)
	# 		if form.is_valid():
	# 			agenda = form.save(commit=False)
	# 			agenda.save()
	# 			return redirect('agenda.html',pk=conference.id)
	# 	else:
	# 		form = AgendaForm(pk=conference.id)
	# 	return render(request, 'agenda.html', {'form': form})

	def get_success_url(self, **kwargs):
		return self.object.get_absolute_url()



class AgendaView(ListView):
	template_name = 'agenda.html'
	queryset = Conference.objects.all()

	def get_context_data(self, **kwargs):
		context = super(AgendaView, self).get_context_data(**kwargs)
		if len(self.queryset)>0:
			context['conf'] = self.queryset[0]

		else:
			context['conf'] = None
		context['agenda'] = Agenda.objects.all()
		return context
     
    