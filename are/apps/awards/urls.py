from django.urls import path
from . import views
from .views import sendMail
from django.contrib.auth.decorators import login_required
app_name = 'awards'

urlpatterns = [
	path('agenda/',login_required(views.AdminAgenda.as_view()),name='admin_agenda'),
	path('challange_award/',views.ChallengeAward.as_view(),name='challenge_award'),
	path('amg_awards/',views.AmgAward.as_view(),name='amg_award'),
	path('award/',views.Award.as_view(),name='award'),
	path('application/',views.ApplicationForm.as_view(),name='application'),
	path('',views.HomePage.as_view(),name='home'),
	path('ourpartner/',views.Partner.as_view(),name='partner'),
	path('agenda/',views.Agenda.as_view(),name='agenda'),
	path('context/',views.Context.as_view(),name='context'),
	path('thankyou/',views.Thankyou.as_view(),name='thankyou'),
	path('sendmail/',sendMail,name='email'),
]
