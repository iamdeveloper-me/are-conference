from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.shortcuts import redirect
from .models import AmgAward, Award
from .forms import AmgApplicationForm
from django.contrib import auth, messages
from django.contrib.auth import logout
# from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(TemplateView):
	template_name = "homepage.html"

class AdminAgendaView(TemplateView):
	template_name = "agenda.html"

class AgendaView(TemplateView): 
	template_name = "agenda.html"

class ContextView(TemplateView):
	template_name = "context.html"

class ChallengeAwardView(TemplateView):
	template_name = "challange_award.html"

class AmgAwardView(TemplateView):
	template_name = "amg_awards.html"

class AwardView(TemplateView):
	template_name = "award.html"

class ApplicationFormView(CreateView):
	model = AmgAward
	form_class = AmgApplicationForm
	template_name = "applicationform.html"
	success_url = '/thanks'

	def post(self, request, *args, **kwargs):
		form = self.get_form()
		if form.is_valid():
			form.save()
			return redirect('awards:thanks')
		else:
			return self.form_invalid(form)

class PartnerView(TemplateView):
	template_name = "ourpartner.html"

class ThanksEnergyView(TemplateView):
	template_name = "thank.html"

class AdminViewAmgApplicant(ListView):
	model = AmgAward
	template_name = 'admin/admin_view_amg_applicants.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context = AmgAward.objects.all().order_by('id')
		return {'context':context}


class AdminDetailViewAmgApplicant(DetailView):
	model = AmgAward
	template_name = 'admin/admin_detail_view_amg_applicants.html'




