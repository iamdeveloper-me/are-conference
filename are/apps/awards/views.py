from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.shortcuts import redirect
from .models import AmgAward
from .forms import AmgApplicationForm

# Create your views here.

class HomePage(TemplateView):
	template_name = "homepage.html"

class Agenda(TemplateView):
	template_name = "agenda.html"

class Context(TemplateView):
	template_name = "context.html"

class ChallengeAward(TemplateView):
	template_name = "challange_award.html"

class AmgAward(TemplateView):
	template_name = "amg_awards.html"

class Award(TemplateView):
	template_name = "award.html"

class ApplicationForm(CreateView):
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

class Partner(TemplateView):
	template_name = "ourpartner.html"


class ThanksEnergy(TemplateView):
	template_name = "thank.html"

