from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save

class Journal(models.Model):
	title = models.CharField(max_length = 100)

	text_field = models.TextField(max_length = 100)

	slug = models.SlugField(unique=True,default="")

	timestamp = models.DateTimeField(auto_now_add = True)

	last_updated = models.DateTimeField(auto_now = True)

	

	def get_absolute_url(self):
		return reverse("Journals:byId",kwargs = {'input_id':self.id})

	def __str__(self):
		return "{}".format(self.title)
		#return "{}".format(self.timestamp)

def generate_slug(sender,instance,*args,**kwargs):
	instance.slug = slugify(instance.title)

pre_save.connect(generate_slug,sender=Journal)
