from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView 
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.views import LoginView,LogoutView
from speakers.models import Speaker
from awards.models import Award,AmgAward,ClimateAward
from speakers.forms import SpeakerForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib import auth, messages
from django.contrib.auth import login, logout
from django.http import Http404


# Create your views here.
class AdminLogin(LoginView):
	template_name = 'admin/admin_login.html'

	def post(self, request, *args, **kwargs):
		
		form = self.get_form()
		if form.is_valid():
			
			username = request.POST['username']
			password = request.POST['password']
			user = auth.authenticate(username = username, password = password)
			if user is not None and user.is_staff == True:
				login(request, user)
				return redirect('awards:dashboard')
				# return redirect('awards:dashboard')
		else:
			return self.form_invalid(form)

class AdminLogout(LogoutView):
	success_url = '/'


class AdminViewSpeaker(ListView):
	model = Speaker
	template_name = "admin_speaker.html"

# class AdminSpeakerCreateView(CreateView):
# 	model = Speaker
# 	form_class = SpeakerForm
# 	template_name = 'admin_speaker.html'

# 	def post(self, request, *args, **kwargs):
# 		if request.method == 'POST' :
# 			name = request.POST.get("name")
# 			designation = request.POST.get("designation")
# 			detail = request.POST.get("detail")
# 			profile_image = request.POST.get("images")
# 			speaker_register = Speaker(name=name,designation=designation,detail=detail,profile_image=profile_image)
# 			speaker_register.save()

# 		return redirect("/admin_login/adminspeaker")

class AdminViewawards(ListView):
	model = Award
	template_name = "admin_awards.html"

	def get_context_data(self, **kwargs):
		total_speaker = Speaker.objects.all().count()
		total_awards = AmgAward.objects.all().count()
		total_climate = ClimateAward.objects.all().count()

		data = {
			'total_speaker':total_speaker,
			'total_awards':total_awards,
			'total_climate':total_climate,
		}

		return {'data':data} 

class SpeakerDeleteView(DeleteView):
    model = Speaker
    success_url = reverse_lazy("speaker_admin")
    template_name = 'delete.html'



class SpeakerUpdateView(UpdateView):
	# import pdb; pdb.set_trace()
	model = Speaker
	template_name = 'admin_speaker.html'
	fields = ['name','designation','detail','profile_image']

	def get_success_url(self, **kwargs):
		return self.object.get_absolute_url()






