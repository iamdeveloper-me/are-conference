from django.shortcuts import render
from .models import Speaker 
from speakers.forms import SpeakerForm
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.

class ViewSpeaker(ListView):
	model = Speaker
	template_name = "speaker.html"

# class SpeakerCreateView(CreateView):
# 	model = Speaker
# 	form_class = SpeakerForm

def AddSpeaker(request):
	if request.method == 'POST' :
		name = request.POST.get("name")
		designation = request.POST.get("designation")
		detail = request.POST.get("detail")
		profile_image = request.POST.get("profile_image")
		speaker_register = Speaker(name=name,designation=designation,detail=detail,profile_image=profile_image)
		speaker_register.save()

		return redirect("speakers/speaker")

	# def get_success_url(self, **kwargs):
	# 	return self.object.get_absolute_url()

