from django.urls import path
from .models import AmgAward
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'awards'

urlpatterns = [
	# path('admin/dashboard/',views.DashboardView.as_view(),name='dashboard'),
	path('challange_award/',views.ChallengeAwardView.as_view(),name='challenge_award'),
	path('amg_awards/',views.AmgAwardView.as_view(),name='amg_award'),
	path('award/',views.AwardView.as_view(),name='award'),
	path('application/',views.AmgApplicationFormView.as_view(),name='application'),
	path('',views.HomePageView.as_view(),name='home'),
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
	path('sendmail/',views.sendMail,name='email'),
	path('shell-gamechanger/',views.Shellgamechanger.as_view(),name='shell-gamechanger'),
	path('session_detail/',views.SessionDetail.as_view(),name='session_detail'),
	path('are_conference2022/',views.AreConference2022.as_view(),name='are_conference2022'),
	path('are_conference2023/',views.AreConference2023.as_view(),name='are_conference2023'),
    path('sponsors/',views.sponsors.as_view(),name='sponsors'),
	path('Sawraj_award2022/',views.Sawrajaward.as_view(),name='Sawraj_award2022'),
	path('media-img/',views.Media.as_view(),name='media-img'),
	path('media/',views.MediaFront.as_view(),name='media'),
	path('register/',views.Register.as_view(),name='register'),
    path('media-detail/',views.Mediadetail.as_view(),name='media-detail'),   
	path('swaraj_award2023/',views.Swarajaward2023.as_view(),name='swaraj_award2023'),   

	
	
	


	# path('agenda_detail/',views.Adminagenda.as_view(),name='agenda_detail'),
	# path('speaker/',views.Adminspeker.as_view(),name='speaker'),
	# path('awards/',views.Adminaward.as_view(),name='awards'),
	# path('dashboard/',views.dashboard.as_view(),name='dashboard'),
	path('text-file/<int:pk>', views.text_file, name='text-file'),
	path('text-file1/<int:pk>', views.text_file1, name='text-file1'),

]