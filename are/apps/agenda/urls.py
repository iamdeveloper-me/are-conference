from django.urls import path
from . import views

app_name = 'agenda'
urlpatterns = [
	path('',views.AgendaView.as_view(),name='agenda_list'),
	path('conferenceadd/',views.ConferenceCreateView.as_view(),name='conference_add'),
	path('agenda_add/',views.MyFormView.as_view(),name='agenda_add'),
	# path('agenda_add/',views.agenda_new,name='agenda_add'),
	path('edit-session-popup/',views.edit_session_popup,name='edit_session_popup'),

	]
