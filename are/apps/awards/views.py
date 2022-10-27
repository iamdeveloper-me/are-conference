from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .models import AmgAward, Award, ClimateAward
from speakers.models import Speaker
from awards.models import Award,AmgAward,ClimateAward
from agenda.models import Seats
from .forms import AmgApplicationForm, ChallengeForm, EmailForm
from django.contrib import auth, messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, JsonResponse

class HomePageView(TemplateView):
	model = Seats
	template_name = "homepage.html"

	def get_context_data(self, **kwargs):
		context = None
		# import pdb; pdb.set_trace()	
		data = Seats.objects.all()
		for item in data:
			context = item
			break
		return {'context':context}	

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

class PartnerView(TemplateView):
	template_name = "ourpartner.html"

class ThanksEnergyView(TemplateView):
	template_name = "thank.html"

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

# class Adminaward(TemplateView):
# 	template_name = 'admin_award.html'

# class Adminagenda(TemplateView):
# 	template_name = 'admin-agenda.html'

# class dashboard(TemplateView):
# 	template_name = 'dashboard.html'
	