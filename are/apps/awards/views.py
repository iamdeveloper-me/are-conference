from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Award
from django.contrib import auth, messages
from django.contrib.auth import logout
from django.shortcuts import redirect
# from django.contrib.auth.mixins import LoginRequiredMixin


class HomePage(TemplateView):
	template_name = "homepage.html"


class AdminAgenda(TemplateView):
	template_name = "agenda.html"

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

class ApplicationForm(TemplateView):
	model = Award
	template_name = "applicationform.html"

class Partner(TemplateView):
	template_name = "ourpartner.html"


class Thankyou(TemplateView):
	template_name = "thank.html"


class Privacypolicy(TemplateView):
	template_name = 'privacy_policy.html'

class climatetable(TemplateView):
	template_name = 'climate_table.html'

class applicationform(TemplateView):
	template_name = 'application_form.html'

