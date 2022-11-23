from django.shortcuts import render
from .models import Speaker 
from speakers.forms import SpeakerForm
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

	
# Create your views here.

class SpeakerView(ListView):
	model = Speaker
	template_name = "speaker.html"
	ordering = ['id']


class SpeakerCreateView(CreateView):
	model = Speaker
	form_class = SpeakerForm

	def get_success_url(self, **kwargs):
		return self.object.get_absolute_url()


