from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Award
<<<<<<< HEAD
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.
=======
from django.contrib import auth, messages
from django.contrib.auth import logout
from django.shortcuts import redirect
# from django.contrib.auth.mixins import LoginRequiredMixin

>>>>>>> dev

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


<<<<<<< HEAD

def sendmail(request):
	import pdb; pdb.set_trace()
	email = request.POST.get('email', '')
	if request.method == 'POST' and email:
		send_mail(subject, content, settings.EMAIL_HOST_USER, ['kuldeep.thoughtwin@gmail.com'], fail_silently=False)
	return render(request, 'home.html',{'email':email})



	# if request.method=='POST':
	# 	email = request.POST.get('email')
	# 	print(email)
	# 	return render('home.html')







# def sendmail(request):

#     send_mail(
#         'Thank you for suscribing ARE conferense',
#         'WelCome to Are conferense ',
#         'kuldeep.thoughtwin@gmail.com',
#         ['dipesh@thoughtwin.com'],
#         fail_silently=False,
#     )

#     return HttpResponse('Mail successfully sent')
=======
>>>>>>> dev
