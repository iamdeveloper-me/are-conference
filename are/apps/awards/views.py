from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Award
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

class ApplicationForm(TemplateView):
	model = Award
	template_name = "applicationform.html"

class Partner(TemplateView):
	template_name = "ourpartner.html"

