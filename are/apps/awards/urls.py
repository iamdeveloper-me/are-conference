from django.urls import path
from .models import AmgAward
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'awards'

urlpatterns = [
	path('agenda/',views.AdminAgendaView.as_view(),name='admin_agenda'),
	path('challange_award/',views.ChallengeAwardView.as_view(),name='challenge_award'),
	path('amg_awards/',views.AmgAwardView.as_view(),name='amg_award'),
	path('award/',views.AwardView.as_view(),name='award'),
	path('application/',views.ApplicationFormView.as_view(),name='application'),
	path('',views.HomePageView.as_view(),name='home'),
	path('ourpartner/',views.PartnerView.as_view(),name='partner'),
	path('agenda/',views.AgendaView.as_view(),name='agenda'),
	path('context/',views.ContextView.as_view(),name='context'),
	path('thanks/',views.ThanksEnergyView.as_view(),name='thanks'),
	# path('amg/',views.amg_applicant,name='amg_applicant'),
	path('amg_applicants/',views.AdminViewAmgApplicant.as_view(), name='amg_applicants'),
	path('amg_applicants/<int:pk>',views.AdminDetailViewAmgApplicant.as_view(), name='amg_applicant_detail'),
]
