from django.urls import path
from .models import AmgAward
from . import views
# from django.contrib.auth.decorators import login_required

app_name = 'awards'

urlpatterns = [

	path('agenda/',views.AdminAgendaView.as_view(),name='admin_agenda'),
	path('challange_award/',views.ChallengeAwardView.as_view(),name='challenge_award'),
	path('amg_awards/',views.AmgAwardView.as_view(),name='amg_award'),
	path('award/',views.AwardView.as_view(),name='award'),
	path('application/',views.AmgApplicationFormView.as_view(),name='application'),
	path('',views.HomePageView.as_view(),name='home'),
	path('ourpartner/',views.PartnerView.as_view(),name='partner'),
	path('agenda/',views.AgendaView.as_view(),name='agenda'),
	path('context/',views.ContextView.as_view(),name='context'),
	path('thanks/',views.ThanksEnergyView.as_view(),name='thanks'),
	path('amg_applicants/',views.AdminViewAmgApplicant.as_view(), name='amg_applicants'),
	path('amg_applicants/<int:pk>',views.AdminDetailViewAmgApplicant.as_view(), name='amg_applicant_detail'),
	path('application_form/',views.ClimateApplicationForm.as_view(),name='climate_application_form'),
	path('privacy_policy/',views.Privacypolicy.as_view(),name='privacy_policy'),
	path('climate_table/',views.ClimateTable.as_view(),name='climate_table'),
	path('climate_1/',views.ClimateApplicationFormOne.as_view(),name='climate_1'),
	path('climate_2/',views.ClimateApplicationFormTwo.as_view(),name='climate_2'),
	path('climate_3/',views.ClimateApplicationFormThree.as_view(),name='climate_3'),
	path('climate_4/',views.ClimateApplicationFormFour.as_view(),name='climate_4'),
	path('climate_5/',views.ClimateApplicationFormFive.as_view(),name='climate_5'),
	path('climate_6/',views.ClimateApplicationFormSix.as_view(),name='climate_6'),
	path('climate_7/',views.ClimateApplicationFormSeven.as_view(),name='climate_7'),
	path('climate_8/',views.ClimateApplicationFormEight.as_view(),name='climate_8'),
	
]
