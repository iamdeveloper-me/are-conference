from django import forms
from .models import AmgAward, ClimateAwardOne, ClimateAwardTwo, ClimateAwardThree, ClimateAwardFour, ClimateAwardFive, ClimateAwardSix, ClimateAwardSeven, ClimateAwardEight

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

class ChallengeFormOne(forms.ModelForm):
	class Meta:
		model = ClimateAwardOne
		fields = [ 'participant', 'full_name', 'email', 'phone_number', 'org_college_name', 
					'designation', 'address_line_one', 'address_line_two', 'address_landmark',
					'city', 'state', 'pincode', 'brief_description', 'working_video', 'steps',
					'major_climate_challenge' ]

class ChallengeFormTwo(forms.ModelForm):
	class Meta:
		model = ClimateAwardTwo
		fields = [ 'full_name', 'email', 'phone_number', 'org_college_name', 
					'designation', 'address_line_one', 'address_line_two', 'address_landmark',
					'city', 'state', 'pincode', 'file' ]

class ChallengeFormThree(forms.ModelForm):
	class Meta:
		model = ClimateAwardThree
		fields = [ 'full_name', 'email', 'phone_number', 'org_college_name', 
					'designation', 'address_line_one', 'address_line_two', 'address_landmark',
					'city', 'state', 'pincode', 'file' ]

class ChallengeFormFour(forms.ModelForm):
	class Meta:
		model = ClimateAwardFour
		fields = [ 'full_name', 'email', 'phone_number', 'org_college_name', 
					'designation', 'address_line_one', 'address_line_two', 'address_landmark',
					'city', 'state', 'pincode', 'file' ]

class ChallengeFormFive(forms.ModelForm):
	class Meta:
		model = ClimateAwardFive
		fields = [ 'full_name', 'email', 'phone_number', 'org_college_name', 
					'designation', 'address_line_one', 'address_line_two', 'address_landmark',
					'city', 'state', 'pincode', 'file' ]

class ChallengeFormSix(forms.ModelForm):
	class Meta:
		model = ClimateAwardSix
		fields = [ 'full_name', 'email', 'phone_number', 'org_college_name', 
					'designation', 'address_line_one', 'address_line_two', 'address_landmark',
					'city', 'state', 'pincode', 'your_view', 'title_song', 'file' ]

class ChallengeFormSeven(forms.ModelForm):
	class Meta:
		model = ClimateAwardSeven
		fields = [ 'full_name', 'email', 'phone_number', 'org_college_name', 
					'designation', 'address_line_one', 'address_line_two', 'address_landmark',
					'city', 'state', 'pincode', 'your_view', 'title_drama', 'file' ]

class ChallengeFormEight(forms.ModelForm):
	class Meta:
		model = ClimateAwardEight
		fields = [ 'full_name', 'email', 'phone_number', 'org_college_name', 
					'designation', 'address_line_one', 'address_line_two', 'address_landmark',
					'city', 'state', 'pincode', 'your_view', 'send_tshirt', 'file' ]
