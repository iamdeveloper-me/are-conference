from django.urls import path
from .models import AmgAward
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'awards'

urlpatterns = [

	# path('dashboard/',views.DashboardView.as_view(),name='dashboard'),
	path('challange_award/',views.ChallengeAwardView.as_view(),name='challenge_award'),
	path('amg_awards/',views.AmgAwardView.as_view(),name='amg_award'),
	path('award/',views.AwardView.as_view(),name='award'),
	path('dashboard/',views.DashboardView.as_view(),name='dashboard'),
	path('application/',views.AmgApplicationFormView.as_view(),name='application'),
	path('',views.HomePage.as_view(),name='home'),
	path('ourpartner/',views.PartnerView.as_view(),name='partner'),
	path('context/',views.ContextView.as_view(),name='context'),
	path('thanks/',views.ThanksEnergyView.as_view(),name='thanks'),
	path('amg_applicants/',views.AdminViewAmgApplicant.as_view(), name='amg_applicants'),
	path('amg_applicants/<int:pk>',views.AdminDetailViewAmgApplicant.as_view(), name='amg_applicant_detail'),
	path('application_form/<int:pk>',views.ClimateApplicationForm.as_view(),name='climate_application_form'),
	path('privacy_policy/',views.Privacypolicy.as_view(),name='privacy_policy'),
	path('climate_table/',views.ClimateTable.as_view(),name='climate_table'),
	path('terms_services/',views.Termsservices.as_view(),name='terms_services'),
	path('climate_applicants/',views.AdminViewClimateApplicant.as_view(),name='climate_applicants'),
	path('climate_applicants/<int:pk>',views.AdminDetailViewClimateApplicant.as_view(), name='climate_applicants_detail'),
	path('dashboard/',views.dashboard.as_view(),name='dashboard'),
	path('sendmail/',views.sendMail,name='email'),
	path('shell-gamechanger/',views.Shellgamechanger.as_view(),name='shell-gamechanger'),
	path('speaker/',views.Adminspeker.as_view(),name='speaker'),
	path('awards/',views.Adminaward.as_view(),name='awards'),
	path('agenda_detail/',views.Adminagenda.as_view(),name='agenda_detail'),

]
path('shell-gamechanger/',views.DashboardView.as_view(),name='dashboard'),