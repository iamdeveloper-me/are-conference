from django.db import models
from django.urls import reverse

# Create your models here.
class Speaker(models.Model):
	name = models.CharField(max_length=155)
	profile_image = models.ImageField(null=True, blank=True,upload_to="images")
	designation = models.CharField(max_length=255,null=True)
	detail = models.TextField()

	def get_absolute_url(self):
		return reverse('speakers:speaker_list')



	