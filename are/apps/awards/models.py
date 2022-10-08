from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

WORK_CHOICES = (
        ('Completed: Application for work already done','Com'),
        ('In Progress: Application for work in progress or is planned in the immediate future','InPro'),
    )
APPLY_FOR = (
    	('Individual','Ind'),
    	('Organization','Org'),
	)
NOMINATION_TYPE = (
    	('Self','S'),
    	('Nominating Other','O'),
	)
AWARD_CATE = (
	('Only avoid','a'),
    ('Only Minimize','m'),
    ('Only Generate','g'),
    ('Avoid and Minimize','a&m'),
    ('Avoid,Minimize and Generate','a,m&g'),
	)


class Award(models.Model):
	name = models.CharField(blank=True, max_length=255)
	title = models.CharField(blank=True,max_length=255)
	description = models.TextField(default=False)
	image = models.ImageField(upload_to='images/awards_forms/', blank=True, null=True)


class AmgAward(models.Model):
	# award_type = models.ForeignKey(Award, related_name='award_type_amg', on_delete=models.CASCADE)
	is_admin = models.BooleanField(default=False)
	email = models.EmailField(unique=True, blank=True)
	work_status = models.CharField(max_length=255,choices=WORK_CHOICES,null=True, blank=True)
	apply_type = models.CharField(max_length=255,choices=APPLY_FOR,null=True, blank=True)
	nomination_type = models.CharField(max_length=255,choices=NOMINATION_TYPE,null=True, blank=True)
	full_name = models.CharField(max_length=255,null=True, blank=True)
	designation = models.CharField(max_length=255,null=True, blank=True)
	phone_number = models.CharField(max_length=255,null=True, blank=True)
	website = models.TextField(max_length=255,null=True, blank=True)
	address = models.TextField(null=True, blank=True)
	org_type = models.CharField(max_length=255,null=True, blank=True)
	org_name = models.CharField(max_length=255,null=True, blank=True)
	org_person_name = models.CharField(max_length=255,null=True,	 blank=True)
	org_person_designation = models.CharField(max_length=255,null=True, blank=True)
	org_person_email = models.EmailField(null=True, blank=True)
	org_person_mobile = models.CharField(max_length=255,null=True, blank=True)
	org_address = models.CharField(max_length=255,null=True, blank=True)
	org_web = models.CharField(max_length=255,null=True, blank=True)
	work_exp = models.TextField(null=True, blank=True)
	interpretation = models.TextField(max_length=300, null=True, blank=True)
	climate_change_challenge = models.TextField(null=True, blank=True)
	award_category = models.CharField(max_length=255,choices=AWARD_CATE,null=True, blank=True)
	target_status = models.CharField(max_length=255, null=True, blank=True)
	target_completed = models.TextField(null=True, blank=True)
	ongoing_invitation_summary = models.TextField(null=True, blank=True)
	invitation_summary = models.TextField(null=True, blank=True)
	challenge_in_invitation = models.TextField(null=True, blank=True)
	implement_invitation = models.TextField(null=True, blank=True)
	amg_image_before = models.FileField(null=True, blank=True,upload_to="images/awards_forms/")
	amg_image_after = models.FileField(null=True, blank=True,upload_to="images/awards_forms/")


class ClimateAward(models.Model):
	challenge_number = models.IntegerField()
	participant = models.CharField(max_length=255, null=True, blank=True)
	full_name = models.CharField(max_length=255, null=True, blank=True)
	email = models.EmailField(blank=True, null=True)
	phone_number = models.CharField(max_length=255,null=True, blank=True)
	org_college_name = models.CharField(max_length=255,null=True, blank=True)
	designation = models.CharField(max_length=255,null=True, blank=True)
	address_line_one = models.TextField(null=True, blank=True)
	address_line_two = models.TextField(null=True, blank=True)
	address_landmark = models.TextField(null=True, blank=True)
	city = models.CharField(max_length=255,null=True, blank=True)
	state = models.CharField(max_length=255,null=True, blank=True)
	pincode = models.IntegerField()
	brief_description = models.TextField(null=True, blank=True, max_length=100)
	major_climate_challenge = models.TextField(null=True, blank=True)
	steps = models.TextField(null=True, blank=True)
	your_view = models.CharField(max_length=255, null=True, blank=True)
	title_song = models.CharField(max_length=255, null=True, blank=True)
	title_drama = models.CharField(max_length=255, null=True, blank=True)
	send_tshirt = models.CharField(max_length=255, null=True, blank=True)
	file = models.FileField(upload_to="images/awards_forms/", blank=True, null=True)
	working_video = models.FileField(upload_to="images/awards_forms/", blank=True, null=True)

