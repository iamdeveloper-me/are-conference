from django.urls import path
from . import views

app_name = 'speakers'
urlpatterns = [
   path('',views.ViewSpeaker.as_view(),name='speaker'),
]    

