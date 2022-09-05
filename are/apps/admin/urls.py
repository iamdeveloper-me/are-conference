from django.urls import path
from . import views

urlpatterns = [
	path('', views.AdminLogin.as_view(), name='admin_login'),
	path('addspeaker/', views.SpeakerCreateView.as_view(), name='speaker_add'),
	path('speaker/', views.AdminViewSpeaker.as_view(), name='speaker_admin'),
	path('deletespeaker/<int:pk>', views.SpeakerDeleteView.as_view(), name='speaker_delete'),
	path('updatespeaker/<int:pk>', views.SpeakerUpdateView.as_view(), name='speaker_update'),
]
