from django.shortcuts import render ,redirect
from django.views.generic import TemplateView
from agenda.models import Agenda,Conference
from agenda.forms import AgendaForm, ConferenceForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class ConferenceView(ListView):
	form_class = AgendaForm
	template_name = 'agenda.html'
	# success_url = reverse_lazy('agenda:agenda')


class ConferenceCreateView(CreateView):
	model = Conference
	form_class = ConferenceForm

	def get_success_url(self, **kwargs):
		return self.object.get_absolute_url()



class AgendaView(ListView):
	model = Agenda
	template_name = 'agenda.html'
	# import pdb; pdb.set_trace()
	# queryset = Agenda.objects.all()
	
	def get_context_data(self, **kwargs):
		# import pdb; pdb.set_trace()
		context = super().get_context_data(**kwargs)
		context['reports_list'] = Agenda.objects.all().order_by('id')
		return context
	# def get_queryset(self):
	# 	import pdb; pdb.set_trace()
	# 	return Agenda.objects.all().order_by('id')

	# def get_context_data(self, **kwargs):
	# 	import pdb; pdb.set_trace()
	# 	context = super().get_context_data(**kwargs)
	# 	context = Agenda.objects.all().order_by('id')
	# 	return {'context':context}


def AddAgenda(request):
	if request.method == 'POST' :
		session = request.POST.get("session")
		starttime = request.POST.get("starttime")
		endtime = request.POST.get("endtime")
		duration = request.POST.get("duration")
		event = request.POST.get("event")
		agenda_register = Agenda(session=session,starttime=starttime,endtime=endtime,duration=duration,event=event)
		agenda_register.save()

	return redirect("agenda:agenda_list")

	def get_success_url(self, **kwargs):
		return self.object.get_absolute_url()

	


	# success_url = reverse_lazy('agenda.html')	
# def AddConference(request):
# 	if request.method == 'POST' :
# 		import pdb; pdb.set_trace()
# 		title = request.POST.get("session")
# 		startdate = request.POST.get("starttime")
# 		enddate = request.POST.get("endtime")
# 		conference_register = Conference(title=title,startdate=startdate,enddate=enddate)
# 		conference_register.save()

# 	return redirect("agenda")


# class AgendaDeleteView(DeleteView):
#     model = Agenda
#     template_name = 'delete.html'
#     def get_success_url(self, **kwargs):
#     	return self.object.get_absolute_url()

# class AgendaUpdateView(UpdateView):
#     model = Agenda
#     template_name = 'update.html'
#     fields = ['session', 'starttime', 'endtime', 'duration', 'event']

    # def get_success_url(self, **kwargs):
    # 	return self.object.get_absolute_url()





# template_name = 'agenda.html'
	
	# def form_valid(self, **kwargs):
	# 	return redirect(self.get_success_url())
