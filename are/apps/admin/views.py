from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView 
from django.views.generic.edit import DeleteView, UpdateView
from speakers.models import Speaker
from speakers.forms import SpeakerForm
from django.http import HttpResponseRedirect

# Create your views here.
class AdminLogin(TemplateView):
	template_name = 'admin/admin_home.html'


class AdminViewSpeaker(ListView):
	model = Speaker
	template_name = "admin/admin_speaker.html"

class SpeakerCreateView(CreateView):
	model = Speaker
	form_class = SpeakerForm
	template_name = 'admin/admin_home.html'

	def AddSpeaker(request):
		if request.method == 'POST' :
			name = request.POST.get("name")
			designation = request.POST.get("designation")
			detail = request.POST.get("detail")
			profile_image = request.POST.get("profile_image")
			speaker_register = Speaker(name=name,designation=designation,detail=detail,profile_image=profile_image)
			speaker_register.save()

		return redirect("speakers/speaker")

	def get_success_url(self, **kwargs):
		return self.object.get_absolute_url()


class SpeakerDeleteView(DeleteView):
    model = Speaker
    # success_url = reverse_lazy("admin:speaker_admin")
    template_name = 'speaker_confirm_delete.html'

    def get_success_url(self, **kwargs):
    	return self.object.get_absolute_url()

class SpeakerUpdateView(UpdateView):
    model = Speaker
    template_name = 'speaker_update.html'
    fields = ['name','designation','detail','profile_image']

    def get_success_url(self, **kwargs):
    	return self.object.get_absolute_url()



