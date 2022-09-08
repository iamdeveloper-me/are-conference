from django.shortcuts import render ,redirect
from django.views.generic import TemplateView
from agenda.models import Agenda,Conference
from agenda.forms import AgendaForm, ConferenceForm
from django.views.generic import ListView,View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.


class ConferenceCreateView(CreateView):
	model = Conference 
	fields = ['title', 'startdate','enddate']

	def get_success_url(self, **kwargs):
		return self.object.get_absolute_url()


class AgendaCreateView(CreateView):
	# import pdb;pdb.set_trace()
	model = Agenda 
	fields = ['session', 'starttime','endtime','duration','event']

class AgendaView(ListView):
    context_object_name = 'name'
    template_name = 'agenda.html'
    queryset = Conference.objects.all()

    def get_context_data(self, **kwargs):
        context = super(MyView, self).get_context_data(**kwargs)
        context['agenda'] = Agenda.objects.all()
        context['conf'] = self.queryset
        return context

