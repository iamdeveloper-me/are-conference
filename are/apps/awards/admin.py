from django.contrib import admin
from .models import AmgAward, Award, ClimateAward
from django import forms
# from phonenumber_field.widgets import PhoneNumberPrefixWidget

admin.register(AmgAward)
admin.register(ClimateAward)
admin.register(Award)