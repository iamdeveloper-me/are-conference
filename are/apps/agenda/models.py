from django.db import models
from django.urls import reverse

# Create your models here

class Conference(models.Model):	
	title = models.CharField(max_length=155,null=True,blank=True)
	startdate = models.DateField(null=True,blank=True)
	enddate = models.DateField(null=True,blank=True)

	def get_absolute_url(self):
		return reverse('agenda:agenda_list')  


class Agenda(models.Model):

	conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='agenda')
	session = models.CharField(max_length=55,null=True,blank=True)
	date = models.DateField(blank=True,null=True)
	starttime = models.TimeField(null=True,blank=True)
	endtime = models.TimeField(null=True,blank=True)
	duration = models.DurationField(null=True,blank=True)
	event = models.CharField(max_length=255,null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('created',)

	def get_absolute_url(self):
		return reverse('agenda:agenda_list') 
