from django.shortcuts import render ,redirect,get_object_or_404
from django.views.generic import TemplateView
from agenda.models import Agenda,Conference
from agenda.forms import AgendaForm, ConferenceForm
from django.views.generic import ListView,View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.timezone import now
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
		# conf = get_object_or_404(Conference, pk=pk)
		# obj = Conference.objects.filter(id=self.kwargs['conf'])     
		
		form = AgendaForm(request.POST)
		if form.is_valid():
			agenda = form.save(commit=False)
			agenda.save()
			return redirect('/agenda')
		else:
			form = AgendaForm(pk=conference.id)
		return render(request, 'agenda.html', {'form': form})

	def get_success_url(self, **kwargs):
		return self.object.get_absolute_url()

		
class AgendaView(ListView):
	# context_object_name = 'name'
	template_name = 'agenda.html'
	queryset = Conference.objects.all().order_by('startdate')

	def get_context_data(self, **kwargs):
		context = super(AgendaView, self).get_context_data(**kwargs)
		if len(self.queryset)>0:
			context['conf'] = self.queryset[0]
		else:
			context['conf'] = None

		context['agenda'] = Agenda.objects.all()
		return context

	def get_queryset(self):
	 
		conference = self.queryset[0]
		agenda_list=conference.agenda.all()
		return agenda_list


    
     
    