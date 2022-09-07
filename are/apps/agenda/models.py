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


class Conferense(models.Model):
	title = models.CharField(max_length=155,null=True,blank=True)
	startdate = models.DateField()
	enddate = models.DateField()

	# def __str__(self):
 #        return self.title   


class Agenda(models.Model):
	session = models.CharField(max_length=55,choices=SESSION_CHOICES,null=True,blank=True)
	starttime = models.TimeField()
	endtime = models.TimeField()
	duration = models.DurationField()
	event = models.CharField(max_length=255,null=True,blank=True)

	 # def __str__(self):
  #       return self.session  
