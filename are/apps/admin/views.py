from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView 
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.views import LoginView,LogoutView
from speakers.models import Speaker
from awards.models import Award,AmgAward,ClimateAward
from agenda.models import Conference,Agenda
from speakers.forms import SpeakerForm
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib import auth, messages
from django.contrib.auth import login, logout
from django.http import Http404
import json
import pandas as pd
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class AdminLogin(LoginView):
	template_name = 'admin/admin_login.html'

	def post(self, request, *args, **kwargs):
		
		form = self.get_form()
		if form.is_valid():
			
			username = request.POST['username']
			password = request.POST['password']
			user = auth.authenticate(username = username, password = password)
			if user is not None and user.is_staff == True:
				login(request, user)
				return redirect('admin_dashboard')
		else:
			return self.form_invalid(form)


class AdminLogout(LogoutView):
	success_url = '/'


class DashboardView(LoginRequiredMixin,TemplateView):
	modal = Speaker
	template_name = "dashboard.html"
	login_url='/admin_login/'

	def get_context_data(self, **kwargs):
		total_speaker = Speaker.objects.all().count()
		total_awards = AmgAward.objects.all().count()
		total_climate = ClimateAward.objects.all().count()

		data = {
			'total_speaker':total_speaker,
			'total_awards':total_awards,
			'total_climate':total_climate,
		}
		return {'data':data} 


class AdminViewSpeaker(ListView):
	model = Speaker
	template_name = "admin_speaker.html"

class AdminSpeakerCreateView(CreateView):
	model = Speaker
	form_class = SpeakerForm
	# template_name = 'admin_speaker.html'

	def post(self, request, *args, **kwargs):
		name = request.POST.get("name")
		designation = request.POST.get("designation")
		detail = request.POST.get("detail")
		profile_image = request.FILES['profile_image']
		speaker_register = Speaker(name=name,designation=designation,detail=detail,profile_image=profile_image)
		speaker_register.save()

		return redirect("/admin/speakers/")

class AdminViewawards(ListView):
	model = Speaker
	template_name = "admin_awards.html"

	def get_context_data(self, **kwargs):
		total_speaker = Speaker.objects.all().count()
		total_awards = AmgAward.objects.all().count()
		total_climate = ClimateAward.objects.all().count()

		data = {
			'total_speaker':total_speaker,
			'total_awards':total_awards,
			'total_climate':total_climate,
		}

		return {'data':data} 


class AdminViewagenda(ListView):
	template_name = 'admin_agendas.html'	
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
			agenda = Agenda.objects.all().filter(conference_id = context['conf'].id)

			data = {}
			for index, item in zip(indexlist, datelist):
				if agenda:
					data[str(index)] = {
						'date':item.date(),
						'data':agenda.filter(date=item.date()).order_by('starttime')
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


class SpeakerDeleteView(DeleteView):
    model = Speaker
    success_url = reverse_lazy("speaker_admin")
    template_name = 'delete.html'



class SpeakerUpdateView(UpdateView):
	model = Speaker
	form_class = SpeakerForm
	template_name = 'admin_speaker.html'
	fields = ['name','designation','detail','profile_image']

	def get_success_url(self, **kwargs):
		return self.object.get_absolute_url()

def edit_speaker_popup(request):
	if request.method =='GET':

		speaker_id = request.GET.get('speaker_id')
		speaker=Speaker.objects.get(id=speaker_id)

		context = {
			'speaker_id':speaker.id,
			'speaker_name':speaker.name,
			'speaker_desig':speaker.designation,
			'speaker_detail':speaker.detail,
			'speaker_profile':speaker.profile_image.url,
		}

		return JsonResponse(context)

	if request.method =='POST':

		speaker_id = request.POST.get('speaker_id')
		speaker_name = request.POST.get('name')
		speaker_desig = request.POST.get('designation')
		speaker_detail = request.POST.get('detail')
		speaker_profile = request.FILES['profile_image']

		speaker = Speaker.objects.get(id=int(speaker_id))
		speaker.name=speaker_name
		speaker.designation=speaker_desig
		speaker.detail=speaker_detail
		speaker.profile_image=speaker_profile

		speaker.save()

		return redirect("/admin/speakers/")
		

def edit_agenda_popup(request):
	if request.method =='GET':
		agenda_id = request.GET.get('agenda_id')
		agenda = Agenda.objects.get(id=agenda_id)
		speaker = Speaker.objects.all()
		data = speaker.values_list('pk','name')
		data1 = list(data)
		all_speakers = []
		for items in data1:
			res_dct = {
				'id':items[0],
				'name':items[1]
			}
			# res_dct = {item[i]: item[i + 1] for i in range(0, len(item), 2)}
			all_speakers.append(res_dct)

		context = {
			'agenda_id':agenda.id,
			'agenda_date':agenda.date,
			'agenda_session':agenda.session,
			'agenda_start':agenda.starttime,
			'agenda_end':agenda.endtime,
			'agenda_event':agenda.event,
			# 'agenda_speaker_id':agenda.speaker.id,
			# 'agenda_speaker_name':agenda.speaker.name,
			'speakers':all_speakers
		}
		if agenda.speaker:
			context['agenda_speaker_id'] = agenda.speaker.id
			context['agenda_speaker_name'] = agenda.speaker.name

		return JsonResponse(context)

	if request.method =='POST':
		agenda_id = request.POST.get('agenda_id')
		agenda_date = request.POST.get('date')
		agenda_session = request.POST.get('edit-session')
		agenda_start = request.POST.get('starttime')
		agenda_end = request.POST.get('endtime')
		agenda_event = request.POST.get('edit-event')
		speaker_id = request.POST.get('speaker')
		speaker = Speaker.objects.get(id=int(speaker_id))

		agenda = Agenda.objects.get(id=int(agenda_id))
		agenda.session = agenda_session
		agenda.date = agenda_date
		agenda.starttime = agenda_start
		agenda.endtime = agenda_end
		# agenda.duration = 
		agenda.event = agenda_event
		agenda.speaker = speaker

		agenda.save()

		return redirect("/admin/agenda/") 









