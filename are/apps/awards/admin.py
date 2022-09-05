from django.contrib import admin
from .models import AmgAward, Award, AwardSubCategory
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class AmgAwardForm(forms.ModelForm):
    class Meta:
        widgets = {                          # Here
            'phone_number': PhoneNumberPrefixWidget(initial='IN'),
            'org_person_mobile': PhoneNumberPrefixWidget(initial='IN'),
        }


# Register your models here.
@admin.register(AmgAward)
class AmgAwardAdmin(admin.ModelAdmin):
	form = AmgAwardForm
	model = AmgAward

admin.site.register(Award)
admin.site.register(AwardSubCategory)

