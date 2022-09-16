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


	# path('',views.ConferenceView.as_view(),name='conference_list'),
	# path('conference/',views.ConferenceListView.as_view(template_name='agenda.html'),name='conference_list'),
	# path('conference/',views.conferencelist,name='conference_list'),
	# path('agenda_add/',views.AgendaCreateView.as_view(),name='agenda_add'),
	# path('addagenda/',views.AgendaCreateView.as_view(),name='agenda_add'),
	# path('conferencedelete/',views.ConferenceDeleteView.as_view(),name='conference_delete'),
	# path('conferenceupdate/',views.ConferenceUpdateView.as_view(),name='conference_update'),
	# path('deleteagenda/',views.AgendaDeleteView.as_view(),name='delete_agenda'),
	# path('updateagenda/',views.AgendaUpdateView.as_view(),name='update_agenda'),