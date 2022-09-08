from django.urls import path
from . import views

app_name = 'agenda'
urlpatterns = [
	# path('',views.ConferenceView.as_view(),name='conference_list'),
	path('conferenceadd/',views.ConferenceCreateView.as_view(),name='conference_add'),
	path('',views.ConferenceListView.as_view(),name='conference_list'),
	path('agenda_add/',views.AgendaCreateView.as_view(),name='agenda_add'),
	path('',views.AgendaListView.as_view(),name='agenda_list'),
	# path('addagenda/',views.AgendaCreateView.as_view(),name='agenda_add'),
	# path('conferencedelete/',views.ConferenceDeleteView.as_view(),name='conference_delete'),
	# path('conferenceupdate/',views.ConferenceUpdateView.as_view(),name='conference_update'),
	# path('deleteagenda/',views.AgendaDeleteView.as_view(),name='delete_agenda'),
	# path('updateagenda/',views.AgendaUpdateView.as_view(),name='update_agenda'),
	]