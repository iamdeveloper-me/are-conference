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
		# import pdb;pdb.set_trace()        
		if request.method == 'POST':
			session = request.POST.get("session")
			starttime = request.POST.get("starttime")
			endtime = request.POST.get("endtime")
			duration = request.POST.get("duration")
			event = request.POST.get("event")
			agenda_add=Agenda(session=session,starttime=starttime,endtime=endtime,duration=duration,event=event)						
			agenda_add.save()
		return redirect("/agenda/list")
		# return render(request, 'agenda.html')

# class AgendaCreateView(CreateView):
# 	# import pdb;pdb.set_trace()
# 	model = Agenda 
# 	fields = ['session', 'starttime','endtime','duration','event']
# 	template_name="agenda.html"

# 	def form_valid(self, form):
# 		import pdb;pdb.set_trace()
# 		self.object = form.save()
# 		return super().form_valid(form)

# 	def get_success_url(self, **kwargs):
# 		return self.object.get_absolute_url()

	# def form_valid(self, form):
	# 	return HttpResponseRedirect(self.get_success_url())


class AgendaView(ListView):
    context_object_name = 'name'
    template_name = 'agenda.html'
    queryset = Conference.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AgendaView, self).get_context_data(**kwargs)
        context['agenda'] = Agenda.objects.all()
        context['conf'] = self.queryset
        return context

