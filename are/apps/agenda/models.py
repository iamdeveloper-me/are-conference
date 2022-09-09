from django.db import models
from django.urls import reverse

# Create your models here.
SESSION_CHOICES=(
     	('1','session-1'),
     	('2','session-2'),
     	('3','session-3'),
     	('4','session-4'),
     	('5','session-5'),
     	('6','session-6'),
     	('7','session-7'),
     	('8','session-8'),
     	('9','session-9'),
     	('10','session-10'),
     	('11','session-11'),
     	('12','session-12'),
	)


class Conference(models.Model):
	title = models.CharField(max_length=155,null=True,blank=True)
	startdate = models.DateField(null=True,blank=True)
	enddate = models.DateField(null=True,blank=True)

	def get_absolute_url(self):
		return reverse('agenda:conference_list')  


class Agenda(models.Model):
	session = models.CharField(max_length=55,choices=SESSION_CHOICES,null=True,blank=True)
	starttime = models.TimeField(null=True,blank=True)
	endtime = models.TimeField(null=True,blank=True)
	duration = models.DurationField(null=True,blank=True)
	event = models.CharField(max_length=255,null=True,blank=True)

	def get_absolute_url(self):
		return reverse('agenda:agenda_list') 