from django import forms
from .models import AmgAward

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

