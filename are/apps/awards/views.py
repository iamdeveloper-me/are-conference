from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Award
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.=
from django.contrib import auth, messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from awards.forms import EmailForm

# from django.contrib.auth.mixins import LoginRequiredMixin


class HomePage(TemplateView):
	template_name = "homepage.html"


class AdminAgenda(TemplateView):
	template_name = "agenda.html"

# class Agenda(TemplateView): 
# 	template_name = "agenda.html"

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

