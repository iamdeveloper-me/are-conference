from django.contrib import admin
from .models import Agenda,Conference,Seats
from django import forms
# Register your models here.

admin.site.register(Conference)
admin.site.register(Agenda)
admin.site.register(Seats)
