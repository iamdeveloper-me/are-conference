from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField

# Create your models here.

WORK_CHOICES = (
        ('Com', 'Completed:Application for work already done'),
        ('InPro', 'Inprogress:Application for work in progress or is planned in the immediate future'),
    )
APPLY_FOR = (
    	('Ind','Individual'),
    	('Org','Orgnization'),
	)
NOMINATION_TYPE = (
    	('S','Self'),
    	('O','Nomanating Other'),
	)
AWARD_CATE = (
	('a','Only awoid'),
    ('m','Only Minimize'),
    ('g','Only Generate'),
    ('a&m','Avoid and Minimize'),
    ('a,m&g','Avoid,Minimize and Generate'),
	)

class AmgAward(models.Model):
	email = models.EmailField(null=True, blank=True)
	work_status = models.CharField(max_length=50,choices=WORK_CHOICES,null=True, blank=True)
	apply_type = models.CharField(max_length=50,choices=APPLY_FOR,null=True, blank=True)
	nomination_type = models.CharField(max_length=50,choices=NOMINATION_TYPE,null=True, blank=True)
	full_name = models.CharField(max_length=155,null=True, blank=True)
	designation = models.CharField(max_length=255,null=True, blank=True)
	phone_number = PhoneNumberField(blank=True, help_text='Contact phone number')
	website = models.URLField(max_length=200,null=True, blank=True)
	address = models.TextField(null=True, blank=True)
	org_type = models.CharField(max_length=155,null=True, blank=True)
	org_name = models.CharField(max_length=155,null=True, blank=True)
	org_person_name = models.CharField(max_length=155,null=True,	 blank=True)
	org_person_designation = models.CharField(max_length=255,null=True, blank=True)
	org_person_email = models.EmailField(null=True, blank=True)
	org_person_mobile = PhoneNumberField(blank=True, help_text='Contact phone number')
	org_address = models.CharField(max_length=255,null=True, blank=True)
	org_web = models.URLField(max_length=200,null=True, blank=True)
	work_exp = models.TextField(null=True, blank=True)
	interpretation = models.TextField(max_length=300, null=True, blank=True)
	climate_change_challenge = models.TextField(null=True, blank=True)
	award_category = models.CharField(max_length=50,choices=AWARD_CATE,null=True, blank=True)
	target_status = models.CharField(max_length=255, null=True, blank=True)
	target_completed = models.TextField(null=True, blank=True)
	ongoing_invitation_summary = models.TextField(null=True, blank=True)
	invitation_summary = models.TextField(null=True, blank=True)
	challenge_in_invitation = models.TextField(null=True, blank=True)
	implement_invitation = models.TextField(null=True, blank=True)
	amg_image_before = models.ImageField(null=True, blank=True,upload_to="images/awards_forms/")
	amg_image_after = models.ImageField(null=True, blank=True,upload_to="images/awards_forms/")


class Award(models.Model):
	name = models.CharField(max_length=255)
	title = models.CharField(max_length=255)
	description = models.TextField()
	image = models.ImageField(upload_to='images/awards_forms/', blank=True, null=True)


class AwardSubCategory(models.Model):
	award_type = models.ForeignKey(Award, related_name='award_type', on_delete=models.CASCADE)
	title = models.CharField(max_length=255)
	participants = models.CharField(max_length=255)
	description = RichTextField(blank=True, null=True)
	submit_by_participants = RichTextField(blank=True, null=True)
	evaluation = RichTextField(blank=True, null=True)
	reward = RichTextField(blank=True, null=True)
	guidelines = RichTextField(blank=True, null=True)
