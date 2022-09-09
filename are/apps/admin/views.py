from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView 
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.views import LoginView,LogoutView
from speakers.models import Speaker
from speakers.forms import SpeakerForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib import auth, messages
from django.contrib.auth import login, logout



# Create your views here.
class AdminLogin(LoginView):
	template_name = 'admin/admin_login.html'

	def post(self, request, *args, **kwargs):
		form = self.get_form()
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = auth.authenticate(username = username, password = password)
			login(request, user)
			if user is not None and user.is_staff == True:
				return redirect('awards:home')
			else:
				return redirect('admin_login')

class AdminLogout(LogoutView):
	success_url = '/'


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






