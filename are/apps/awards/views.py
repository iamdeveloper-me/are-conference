from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.shortcuts import redirect
from .models import AmgAward
from .forms import AmgApplicationForm

# Create your views here.

class HomePage(TemplateView):
	template_name = "homepage.html"

class Agenda(TemplateView):
	template_name = "agenda.html"

class Context(TemplateView):
	template_name = "context.html"

class ChallengeAward(TemplateView):
	template_name = "challange_award.html"

class AmgAward(TemplateView):
	template_name = "amg_awards.html"

class Award(TemplateView):
	template_name = "award.html"

class ApplicationForm(CreateView):
	model = AmgAward
	form_class = AmgApplicationForm
	template_name = "applicationform.html"
	success_url = '/thanks'

	def post(self, request, *args, **kwargs):
		# import pdb;pdb.set_trace(); 
		form = self.get_form()
		if form.is_valid():
			form.save()
			return redirect('awards:thanks')
		else:
			return self.form_invalid(form)	

class Partner(TemplateView):
	template_name = "ourpartner.html"


class ThanksEnergy(TemplateView):
	template_name = "thank.html"

# class AdminViewAmgApplicant(ListView):
# 	model = AmgAward
# 	template_name = 'admin/admin_view_amg_applicants.html'
# 	# queryset = AmgAward.objects.all()

# 	# def get(self, request, *args, **kwargs):
# 	#     self.object_list = self.get_queryset()
# 	#     allow_empty = self.get_allow_empty()	        	
# 	#     context = self.get_context_data()
# 	#     return context
# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		context = AmgAward._default_manager.all()
# 		return {'context':context}

def amg_applicant(request):
	# import pdb;pdb.set_trace()
	data = AmgAward.objects.all()
	return render(request, 'admin/admin_view_amg_applicants.html', {'data':data})


