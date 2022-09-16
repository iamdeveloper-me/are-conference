from django import forms
from speakers.model import Speaker
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
                'username',
                'password',
        ]

class UpdateSpeakerForm(forms.ModelForm):
    class Meta:
        model = Speaker
        fields = [
                'name','profile_image',
                'designation','detail'
        ]