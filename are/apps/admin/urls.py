from django.urls import path
from . import views
# from .views import logout
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
# from django.urls import path, reverse_lazy

# app_name = "admin"

urlpatterns = [
	path('login/', views.AdminLogin.as_view(), name='admin_login'),
    path('logout/', views.AdminLogout.as_view(), name='logout'),
	path('dashboard/',views.DashboardView.as_view(),name='admin_dashboard'),
	path('speakers/', views.AdminViewSpeaker.as_view(), name='speaker_admin'),
	path('awards/', views.AdminViewawards.as_view(), name='awards_admin'),
	path('agenda/', views.AdminViewagenda.as_view(), name='agendas_admin'),
	path('partner/', views.AdminViewPartner.as_view(), name='agendas_partner'),

	path('adminaddspeaker/', views.AdminSpeakerCreateView.as_view(), name='admin_add_speaker'),
	path('deletespeaker/<int:pk>', views.SpeakerDeleteView.as_view(), name='speaker_delete'),
	path('updatespeaker/<int:pk>', views.SpeakerUpdateView.as_view(), name='speaker_update'),
    path('editspeakerpopup/', views.edit_speaker_popup, name='admin_speaker_edit'),
    path('editagendapopup/', views.edit_agenda_popup, name='admin_agenda_edit'),
]
