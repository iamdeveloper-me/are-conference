from django import forms
from .models import AmgAward, ClimateAward

class EmailForm(forms.Form):
    recipient = forms.EmailField()


class AmgApplicationForm(forms.ModelForm):
	class Meta:
		model = AmgAward
		fields = [ 'is_admin', 'email', 'work_status', 'apply_type', 'nomination_type', 'full_name',
					'designation', 'phone_number', 'website', 'address', 'org_type', 'org_name',
					'org_person_name', 'org_person_designation', 'org_person_email',
					'org_person_mobile', 'org_address', 'org_web', 'work_exp', 'interpretation',
					'climate_change_challenge', 'award_category', 'target_status', 
					'target_completed', 'ongoing_invitation_summary', 'invitation_summary',
					'challenge_in_invitation', 'implement_invitation', 'amg_image_before',
					'amg_image_after' ]

	def check_duplicate_email(self):
		data = self.cleaned_data['email']
		if AmgAward.objects.filter(email=data).exists():
			raise forms.ValidationError('Your email is already in our list of users to be notified.Try a new email')

class ChallengeForm(forms.ModelForm):
	class Meta:
		model = ClimateAward
		fields = [ 'challenge_number', 'participant', 'full_name', 'email', 'phone_number', 
					'org_college_name', 'designation', 'address_line_one', 'address_line_two',
					'address_landmark','city', 'state', 'pincode', 'brief_description',
					'working_video', 'steps','major_climate_challenge', 'your_view', 
					'title_song', 'title_drama', 'send_tshirt', 'file' ]


