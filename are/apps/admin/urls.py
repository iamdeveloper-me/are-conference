from django.urls import path
from . import views
# from .views import logout
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
# from django.urls import path, reverse_lazy

urlpatterns = [
	path('', views.AdminLogin.as_view(), name='admin_login'),
	path('adminaddspeaker/', views.AdminSpeakerCreateView.as_view(), name='admin_add_speaker'),
	path('adminspeaker/', views.AdminViewSpeaker.as_view(), name='speaker_admin'),
	path('deletespeaker/<int:pk>', views.SpeakerDeleteView.as_view(), name='speaker_delete'),
	path('updatespeaker/<int:pk>', views.SpeakerUpdateView.as_view(), name='speaker_update'),
    path('logout/', views.AdminLogout.as_view(), name='admin_logout'),
    path('editpopup/', views.edit_speaker_popup, name='admin_speaker_edit'),
]
