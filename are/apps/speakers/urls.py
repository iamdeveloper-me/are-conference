from django.urls import path
from . import views

app_name = 'speakers'
urlpatterns = [
   path('',views.SpeakerView.as_view(),name='speaker_list'),
   path('addspeaker/', views.SpeakerCreateView.as_view(), name='add_speaker'),
   # path('addspeaker/',views.AddSpeaker,name='add_speaker')
]    

