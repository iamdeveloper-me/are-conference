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
	template_name="agenda.html"

	def get_success_url(self, **kwargs):
		return self.object.get_absolute_url()

class MyFormView(CreateView):
	model = Agenda 
	form_class = AgendaForm
	template_name = 'agenda.html'

	def post(self, request, *args, **kwargs):
		obj = Conference.objects.filter(id=kwargs['pk'])[0]
		# obj = get_object_or_404(Conference, pk=pk
		# import pdb;pdb.set_trace()        
		if request.method == 'POST':
			session = request.POST.get("session")
			starttime = request.POST.get("starttime")
			endtime = request.POST.get("endtime")
			duration = request.POST.get("duration")
			event = request.POST.get("event")
			agenda_add=Agenda(session=session,starttime=starttime,endtime=endtime,duration=duration,event=event,obj=obj)						
			agenda_add.save()
		return redirect("agenda")

	def get_success_url(self, **kwargs):
		return self.object.get_absolute_url()


class AgendaView(ListView):
	# context_object_name = 'name'
	template_name = 'agenda.html'
	queryset = Conference.objects.all()

	def get_context_data(self, **kwargs):
		# import pdb; pdb.set_trace()
		context = super(AgendaView, self).get_context_data(**kwargs)
		if len(self.queryset)>0:
			context['conf'] = self.queryset[0]
		else:
			context['conf'] = None
		context['agenda'] = Agenda.objects.all()
		return context

    # context_object_name = 'name'
    # template_name = 'agenda.html'
    # queryset = Conference.objects.all()
    # import pdb; pdb.set_trace()
    
     
    