from django.contrib import admin
from .models import Award
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class AwardForm(forms.ModelForm):
    class Meta:
        widgets = {                          # Here
            'phone_number': PhoneNumberPrefixWidget(initial='IN'),
            'org_person_mobile': PhoneNumberPrefixWidget(initial='IN'),
        }


# Register your models here.
@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
	form = AwardForm
	model = Award
