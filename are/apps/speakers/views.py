from django.shortcuts import render
from .models import Speaker
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.

class ViewSpeaker(ListView):
	model = Speaker
	template_name = "speaker.html"


# class CreateSpeaker(CreateView):
#   	model = Speaker
#   	template_name = "speaker.html"


# class UpdateSpeaker(UpdateView):
# 	model = Speaker
# 	template_name = "speaker.html"
#     fields = ['name','profile_image','designation','detail']


# class DeleteSpeaker(DeleteSpeaker):
# 	model =  Speaker
#     template_name = "speaker.html"
#     success_url = reverse_lazy("speaker")
