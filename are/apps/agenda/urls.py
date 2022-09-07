from django.urls import path
from . import views

app_name = 'agenda'
urlpatterns = [
	path('conf/',views.ConferenseView.as_view(),name='conferense'),
	path('confadd/',views.ConferenseCreateView.as_view(),name='confadd'),
	path('confdel/',views.ConferenseDeleteView.as_view(),name='confdel'),
	path('confupdate/',views.ConferenseUpdateView.as_view(),name='confupdate'),
	path('agenda/',views.AgendaView.as_view(),name='agenda'),
	path('addagenda/',views.AgendaCreateView.as_view(),name='add_agenda'),
	path('deleteagenda/',views.AgendaDeleteView.as_view(),name='delete_agenda'),
	path('updateagenda/',views.AgendaUpdateView.as_view(),name='update_agenda'),
	]