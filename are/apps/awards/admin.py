from django.contrib import admin
from .models import AmgAward, Award, ClimateAward
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class AmgAwardForm(forms.ModelForm):
    class Meta:
        widgets = {                       
            'phone_number': PhoneNumberPrefixWidget(initial='IN'),
            'org_person_mobile': PhoneNumberPrefixWidget(initial='IN'),
        }


class ClimateAwardForm(forms.ModelForm):
    class Meta:
        widgets = {                         
            'phone_number': PhoneNumberPrefixWidget(initial='IN'),
        }


# Register your models here.
@admin.register(AmgAward)
class AmgAwardAdmin(admin.ModelAdmin):
	form = AmgAwardForm
	model = AmgAward

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
	model = Award


@admin.register(ClimateAward)
class ClimateAwardAdmin(admin.ModelAdmin):
    form = ClimateAwardForm
    model = ClimateAward

