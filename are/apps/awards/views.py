from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .models import AmgAward, Award, ClimateAward
from .forms import AmgApplicationForm, ChallengeForm, EmailForm
from django.contrib import auth, messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.conf import settings

class HomePageView(TemplateView):
	template_name = "homepage.html"

class AdminAgendaView(TemplateView):
	template_name = "agenda.html"

# class AgendaView(TemplateView): 
# 	template_name = "agenda.html"

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
	success_url = '/thanks'

	def post(self, request, *args, **kwargs):
		form = self.get_form()
		if form.is_valid():
			form.save()
			return redirect('awards:thanks')
		else:
			return self.form_invalid(form)

class PartnerView(TemplateView):
	template_name = "ourpartner.html"

class ThanksEnergyView(TemplateView):
	template_name = "thank.html"

class AdminViewAmgApplicant(LoginRequiredMixin, ListView):
	model = AmgAward
	template_name = 'admin/admin_view_amg_applicants.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context = AmgAward.objects.all().order_by('id')
		return {'context':context}


class AdminDetailViewAmgApplicant(DetailView):
	model = AmgAward
	template_name = 'admin/admin_detail_view_amg_applicants.html'


class Privacypolicy(TemplateView):
	template_name = 'privacy_policy.html'
	
class Termsservices(TemplateView):
	template_name = 'term_services.html'

class dashboard(TemplateView):
	template_name = 'dashboard.html'

class ClimateTable(TemplateView):
	template_name = 'climate_table.html'

class ClimateApplicationForm(CreateView):
	model = ClimateAward
	template_name = 'application_form.html'
	form_class = ChallengeForm

	def post(self, request, *args, **kwargs):
		form = self.get_form()
		if form.is_valid():
			form.save()
			return redirect('awards:thanks')
		else:
			return self.form_invalid(form)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context = self.kwargs['pk']
		context = {'context':context}
		return context


class AdminViewClimateApplicant(TemplateView):
	model = ClimateAward
	template_name = 'admin/admin_view_climate_applicants.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context = ClimateAward.objects.filter(challenge_number=1)
		challenge_number = 1
		return {'context':context, 'challenge_number':challenge_number}

	def post(self, request, *args, **kwargs):
		challenge_number = int(request.POST.get('challenge_number'))
		context = ClimateAward.objects.filter(challenge_number=challenge_number)
		return render(request, 'admin/admin_view_climate_applicants.html', {'context':context, 'challenge_number':challenge_number})


class AdminDetailViewClimateApplicant(DetailView):
	model = ClimateAward
	template_name = 'admin/admin_detail_view_climate_applicants.html'

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

class Climateaward(TemplateView):
	template_name = 'climate_award.html'