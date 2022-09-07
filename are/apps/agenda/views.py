from django.shortcuts import render
from django.views.generic import TemplateView
from agenda.models import Agenda,Conferense
from agenda.forms import AgendaForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class ConferenseView(ListView):
	template_name = 'agenda.html'
	form_class = AgendaForm
	success_url = reverse_lazy('agenda:agenda')

	def get_queryset(self):
		return Conferense.objects.all()

class ConferenseCreateView(CreateView):
	# model = Conferense
	form_class = AgendaForm
	success_url = 'agenda.html'

	# def form_valid(self, form):
 #        return redirect(self.get_success_url())

	def AddConference(request):
		if request.method == 'POST' :
			title = request.POST.get("session")
			startdate = request.POST.get("starttime")
			enddate = request.POST.get("endtime")
			conferense_register = Conferense()
			conferense_register.save()

		return redirect("agenda.html")

	def get_success_url(self, **kwargs):
		return self.object.get_absolute_url()


class ConferenseDeleteView(DeleteView):
    model = Conferense
    # success_url = reverse_lazy("admin:speaker_admin")
    template_name = 'delete.html'

    def get_success_url(self, **kwargs):
    	return self.object.get_absolute_url()

class ConferenseUpdateView(UpdateView):
    model = Conferense
    template_name = 'update.html'
    fields = ['title', 'startdate', 'enddate']

    def get_success_url(self, **kwargs):
    	return self.object.get_absolute_url()



# agenda session start from 

class AgendaView(ListView):
	template_name = 'agenda.html'
	form_class = AgendaForm
	success_url = reverse_lazy('agenda:agenda')

	def get_queryset(self):
		return Agenda.objects.all()
	# import pdb; pdb.set_trace()
	# model = Agenda

class AgendaCreateView(CreateView):
	# model = Agenda
	form_class = AgendaForm
	template_name = 'agenda.html'

	def AddAgenda(request):
		if request.method == 'POST' :
			session = request.POST.get("session")
			starttime = request.POST.get("starttime")
			endtime = request.POST.get("endtime")
			duration = request.POST.get("duration")
			event = request.POST.get("event")
			agenda_register = Agenda()
			agenda_register.save()

		return redirect("agenda.html")
	def form_valid(self, form):
		return redirect(self.get_success_url())

class AgendaDeleteView(DeleteView):
    model = Agenda
    # success_url = reverse_lazy("admin:speaker_admin")
    template_name = 'delete.html'

    def get_success_url(self, **kwargs):
    	return self.object.get_absolute_url()

class AgendaUpdateView(UpdateView):
    model = Agenda
    template_name = 'update.html'
    fields = ['session', 'starttime', 'endtime', 'duration', 'event']

    def get_success_url(self, **kwargs):
    	return self.object.get_absolute_url()

