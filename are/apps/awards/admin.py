from django.contrib import admin
from .models import AmgAward, Award, ClimateAwardOne, ClimateAwardTwo, ClimateAwardThree, ClimateAwardFour, ClimateAwardFive, ClimateAwardSix, ClimateAwardSeven, ClimateAwardEight
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class AmgAwardForm(forms.ModelForm):
    class Meta:
        widgets = {                          # Here
            'phone_number': PhoneNumberPrefixWidget(initial='IN'),
            'org_person_mobile': PhoneNumberPrefixWidget(initial='IN'),
        }


class ClimateAwardForm(forms.ModelForm):
    class Meta:
        widgets = {                          # Here
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


@admin.register(ClimateAwardOne)
class ClimateAwardOneAdmin(admin.ModelAdmin):
    form = ClimateAwardForm
    model = ClimateAwardOne


admin.site.register(ClimateAwardTwo)
admin.site.register(ClimateAwardThree)
admin.site.register(ClimateAwardFour)
admin.site.register(ClimateAwardFive)
admin.site.register(ClimateAwardSix)
admin.site.register(ClimateAwardSeven)
admin.site.register(ClimateAwardEight)

