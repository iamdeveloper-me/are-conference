from django.contrib import admin
from .models import Speaker

# Register your models here.

@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
	model = Speaker
	list_display = ['id', 'name']
