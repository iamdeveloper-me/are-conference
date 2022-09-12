from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.shortcuts import redirect
from .models import AmgAward, Award, ClimateAwardOne, ClimateAwardTwo, ClimateAwardThree, ClimateAwardFour, ClimateAwardFive, ClimateAwardSix, ClimateAwardSeven, ClimateAwardEight
from .forms import AmgApplicationForm, ChallengeFormOne, ChallengeFormTwo, ChallengeFormThree, ChallengeFormFour, ChallengeFormFive, ChallengeFormSix, ChallengeFormSeven, ChallengeFormEight
from django.contrib import auth, messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(TemplateView):
	template_name = "homepage.html"

class AdminAgendaView(TemplateView):
	template_name = "agenda.html"

class AgendaView(TemplateView): 
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

class ClimateTable(TemplateView):
	template_name = 'climate_table.html'

class ClimateApplicationForm(CreateView):
	template_name = 'application_form.html'

class ClimateApplicationFormOne(CreateView):
	model = ClimateAwardOne
	form_class = ChallengeFormOne
	template_name = 'climate/challenge_form_1.html'

	def post(self, request, *args, **kwargs):
		form = ChallengeFormOne(request.POST)
		for field in form:
			print("Field Error:", field.name,  field.errors)
		form = self.get_form()
		if form.is_valid():
			form.save()
			return redirect('awards:thanks')
		else:
			return self.form_invalid(form)

class ClimateApplicationFormTwo(CreateView):
	model = ClimateAwardTwo
	form_class = ChallengeFormTwo
	template_name = 'climate/challenge_form_2.html'

	def post(self, request, *args, **kwargs):
		form = self.get_form()
		if form.is_valid():
			form.save()
			return redirect('awards:thanks')
		else:
			return self.form_invalid(form)

class ClimateApplicationFormThree(CreateView):
	model = ClimateAwardThree
	form_class = ChallengeFormThree
	template_name = 'climate/challenge_form_3.html'

	def post(self, request, *args, **kwargs):
		form = self.get_form()
		if form.is_valid():
			form.save()
			return redirect('awards:thanks')
		else:
			return self.form_invalid(form)

class ClimateApplicationFormFour(CreateView):
	model = ClimateAwardFour
	form_class = ChallengeFormFour
	template_name = 'climate/challenge_form_4.html'

	def post(self, request, *args, **kwargs):
		form = self.get_form()
		if form.is_valid():
			form.save()
			return redirect('awards:thanks')
		else:
			return self.form_invalid(form)

class ClimateApplicationFormFive(CreateView):
	model = ClimateAwardFive
	form_class = ChallengeFormFive
	template_name = 'climate/challenge_form_5.html'

	def post(self, request, *args, **kwargs):
		form = self.get_form()
		if form.is_valid():
			form.save()
			return redirect('awards:thanks')
		else:
			return self.form_invalid(form)

class ClimateApplicationFormSix(CreateView):
	model = ClimateAwardSix
	form_class = ChallengeFormSix
	template_name = 'climate/challenge_form_6.html'

	def post(self, request, *args, **kwargs):
		form = self.get_form()
		if form.is_valid():
			form.save()
			return redirect('awards:thanks')
		else:
			return self.form_invalid(form)

class ClimateApplicationFormSeven(CreateView):
	model = ClimateAwardSeven
	form_class = ChallengeFormSeven
	template_name = 'climate/challenge_form_7.html'

	def post(self, request, *args, **kwargs):
		form = self.get_form()
		if form.is_valid():
			form.save()
			return redirect('awards:thanks')
		else:
			return self.form_invalid(form)

class ClimateApplicationFormEight(CreateView):
	model = ClimateAwardEight
	form_class = ChallengeFormEight
	template_name = 'climate/challenge_form_8.html'

	def post(self, request, *args, **kwargs):
		form = self.get_form()
		if form.is_valid():
			form.save()
			return redirect('awards:thanks')
		else:
			return self.form_invalid(form)


