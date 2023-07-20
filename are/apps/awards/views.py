from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .models import AmgAward, Award, ClimateAward
from speakers.models import Speaker
from awards.models import Award,AmgAward,ClimateAward,PartnerRegister
from agenda.models import Seats
from .forms import AmgApplicationForm, ChallengeForm, EmailForm, PartnerRegisterForm
from django.contrib import auth, messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from reportlab.pdfgen import canvas
from tabulate import tabulate
from prettytable import PrettyTable
import csv, json, datetime	

class HomePageView(TemplateView):
	model = Seats
	template_name = "homepage.html"

	def get_context_data(self, **kwargs):
		context = None
		data = Seats.objects.all()
		for item in data:
			context = item
			break
		return {'context':context}

class PartnerRegisterView(CreateView):
	model = PartnerRegister 
	form_class = PartnerRegisterForm
	template_name = 'partner_register.html'

	def get_context_data(self,*args, **kwargs):
		context = super(PartnerRegisterView, self).get_context_data(*args,**kwargs)
		data = {}
		data['count_list'] = [item for item in range(2022, datetime.date.today().year+2)]
		# import pdb; pdb.set_trace()	
		return {'data':data}

	def post(self, request, *args, **kwargs):	
		# import pdb; pdb.set_trace()

		# objs = Conference.objects.filter(id=kwargs['pk'])[0]
		form = PartnerRegisterForm(request.POST, request.FILES)
		if form.is_valid():
			data = form.save(commit=False)
			data.save()
			request.session['status']='done'
			status = {
				'status':'success',
			}
			# send_message(
   #              form.cleaned_data['name'],
   #              form.cleaned_data['message']
   #          )
			# kwargs = {"data":True}
			return HttpResponse(json.dumps(status),content_type="application/json")
			# return JsonResponse(status)
		else:
			status = {
				'status':'error',
				'errors':form.errors,
				'data':form.data
			}
			return HttpResponse(json.dumps(status),content_type="application/json")


class SessionDetail(TemplateView):
	template_name = "session_detail.html"

class AreConference2022(TemplateView):
	template_name = "are_conference2022.html"

class AreConference2023(TemplateView):
	template_name = "are_conference2023.html"

class sponsors(TemplateView):
	template_name = "sponsors.html"

class Sawrajaward(TemplateView):
	template_name = "swaraj_award2022.html"

class Mediaimg(TemplateView):
	template_name = "media-img.html"

class MediaFront(TemplateView):
	template_name = "media.html"

class Mediadetail(TemplateView):
	template_name = "media_detail.html"

class Swarajaward2023(TemplateView):
	template_name = "swaraj_award2023.html"

# class Swarajaward2023(TemplateView):
# 	template_name = "media_video.html"

class Register(TemplateView):
	template_name = "partner_register.html"

class AdminAgendaView(TemplateView):
	template_name = "agenda.html"

class ContextView(TemplateView):
	template_name = "context.html"

class ChallengeAwardView(TemplateView):
	template_name = "challange_award.html"

class AmgAwardView(TemplateView):
	template_name = "amg_awards.html"

class AwardView(TemplateView):
	template_name = "award.html"

class AmgApplicationFormView(CreateView):
	model = AmgAward
	form_class = AmgApplicationForm
	template_name = "applicationform.html"
	success_url = '/thanks/'

	def post(self, request, *args, **kwargs):
		# form = self.get_form()
		form_class = self.get_form_class()
		form = form_class(request.POST, request.FILES)
		if form.is_valid():
			data = form.save(commit=False)
			data.save()
			status = {
				'status':'success',
			}
			return JsonResponse(status)
			# return redirect('awards:thanks')
		else:

			errors = form.errors
			error = {}
			for key,value in errors.items():
				error[key]= value[0]
			status = {
				'status':'error',
				'errors':error
			}
			return JsonResponse(status)


# class SpeakerUpdateView(UpdateView):
# 	model = Speaker
# 	form_class = SpeakerForm
# 	template_name = 'admin_speaker.html'
# 	fields = ['name','designation','detail','profile_image']

		# else:
		# 	amg_email = form.data.get('email')
		# 	amg_mobile = form.data.get('phone_number')
		# 	if AmgAward.objects.filter(email=amg_email).exists():
		# 		messages.warning(request, "Email already exists")
		# 	else:
		# 		pass
		# 	if AmgAward.objects.filter(phone_number=amg_mobile).exists():
		# 		messages.warning(request, "Number already exists")

		# 	status = {
		# 		'status':'error'

		# 	}
		# 	return JsonResponse(status)
			# return redirect('application/')


		# else:
		# 	return self.form_invalid(form)
			
	# def form_invalid(self, form):
	#     """If the form is invalid, render the invalid form."""
	#     return self.render_to_response(self.get_context_data(form=form))
class PartnerView(ListView):
	model = PartnerRegister
	template_name = "ourpartner.html"
	ordering = ['id']

	def get_context_data(self,*args, **kwargs):
		# import pdb; pdb.set_trace()
		if 'status' in self.request.session and self.request.session['status']=='done':
			context = {
				'status':'yes',
				'data': PartnerRegister.objects.all()
				}
			del self.request.session['status']
		else:
			context = {
				'status':'no',
				'data':PartnerRegister.objects.all()
				}
		return context



# class PartnerView(TemplateView):
# 	template_name = "ourpartner.html"

	# def get_context_data(self,*args, **kwargs):
	# 	import pdb; pdb.set_trace()
	# 	context = super(PartnerView, self).get_context_data(*args,**kwargs)
	# 	context = {}
	# 	context['users'] = 'hi'
	# 	return context

class ThanksEnergyView(TemplateView):
	template_name = "thank.html"

def text_file(request, pk):
	response = HttpResponse(content_type='text/csv')

	response['Content-Disposition'] = 'attachment; data.csv'
	data = AmgAward.objects.filter(id=pk).values()
	data1 = list(data)	
	lines = [['field', 'values']]	

	for key,value in data1[0].items():
		lines.append([f"{key}" , f"{value}"])
	# c = canvas.Canvas("data.pdf")

	writer = csv.writer(response)
	writer.writerow(["fields","value"])
	for key,value in data1[0].items():
		writer.writerow([f"{key}" , f"{value}"])

	return response

def text_file1(request, pk):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; data.csv'
	data = ClimateAward.objects.filter(id=pk).values()
	data1 = list(data)	
	lines = [['field', 'values']]	

	for key,value in data1[0].items():
		lines.append([f"{key}" , f"{value}"])
	# c = canvas.Canvas("data.pdf")

	writer = csv.writer(response)
	writer.writerow(["fields","value"])
	for key,value in data1[0].items():
		writer.writerow([f"{key}" , f"{value}"])

	return response


class AdminViewAmgApplicant(LoginRequiredMixin, ListView):
	model = AmgAward
	template_name = 'admin/admin_view_amg_applicants.html'
	login_url='/admin/login/'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context = {
			"individual":AmgAward.objects.filter(org_name=None),
			"organization":AmgAward.objects.filter(full_name=None)
		}
		return {'context':context}


class AdminDetailViewAmgApplicant(LoginRequiredMixin, DetailView):
	model = AmgAward
	template_name = 'admin/admin_detail_view_amg_applicants.html'
	login_url='/admin/login/'



class Privacypolicy(TemplateView):
	template_name = 'privacy_policy.html'
	
class Termsservices(TemplateView):
	template_name = 'term_services.html'


class ClimateTable(TemplateView):
	template_name = 'climate_table.html'

class ClimateApplicationForm(CreateView):
	model = ClimateAward
	template_name = 'application_form.html'
	form_class = ChallengeForm

	def post(self, request, *args, **kwargs):
		# form = self.get_form()
		form_class = self.get_form_class()
		form = form_class(request.POST, request.FILES)
		if form.is_valid():
			data = form.save(commit=False)
			data.save()
			status = {
				'status':'success',
			}
			return JsonResponse(status)
			# return redirect('awards:thanks')
		else:
			errors = form.errors
			error = {}
			for key,value in errors.items():
				error[key]= value[0]
			status = {
				'status':'error',
				'errors':error
			}
			return JsonResponse(status)

	# def post(self, request, *args, **kwargs):
	# 	form = self.get_form()
	# 	if form.is_valid():
	# 		form.save()
	# 		return redirect('awards:thanks')
	# 	else:
	# 		return self.form_invalid(form)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context = self.kwargs['pk']
		context = {'context':context}
		return context


class AdminViewClimateApplicant(LoginRequiredMixin, TemplateView):
	model = ClimateAward
	template_name = 'admin/admin_view_climate_applicants.html'
	login_url='/admin/login/'


	def get_context_data(self, **kwargs):
		context = {}
		for i in range(1,9):
			context[i]= {
				"data":ClimateAward.objects.filter(challenge_number=i)
			}
		return {'context':context}


class AdminDetailViewClimateApplicant(LoginRequiredMixin, DetailView):
	model = ClimateAward
	template_name = 'admin/admin_detail_view_climate_applicants.html'
	login_url='/admin/login/'

def sendMail(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = "Sending an email with Django"
            message = "Thank YOu for suscribing as Are"
            send_mail(subject, message,
                      settings.DEFAULT_FROM_EMAIL, [cd['recipient']])
    else:
        form = EmailForm()

    return render(request, 'homepage.html')

class Shellgamechanger(TemplateView):
	template_name = 'climate_award.html'

# class Adminspeker(TemplateView):
# 	template_name = 'admin_speaker.html'

class Session1_Images(TemplateView):
	template_name = 'Session1_images.html'

class Session2_Images(TemplateView):
	template_name = 'Session2_images.html'

class Session3_Images(TemplateView):
	template_name = 'Session3_images.html'

class Session4_Images(TemplateView):
	template_name = 'Session4_images.html'

class Session5_Images(TemplateView):
	template_name = 'Session5_images.html'

class Session6_Images(TemplateView):
	template_name = 'Session6_images.html'

class Session7_Images(TemplateView):
	template_name = 'Session7_images.html'

class Session8_Images(TemplateView):
	template_name = 'Session8_images.html'

class Ebooklaunch(TemplateView):
	template_name = 'E-booklaunch.html'

class ESAphotos(TemplateView):
	template_name = 'ESAphotos.html'

class Expostalls(TemplateView):
	template_name = 'Expostalls.html'

class Randomclick(TemplateView):
	template_name = 'Randomclick.html'

class Shellgamechanger(TemplateView):
	template_name = 'Shell gamechanger.html'

class Inauguration(TemplateView):
	template_name = "inauguration.html"