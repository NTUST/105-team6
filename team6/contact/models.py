from django.db import models

# Create your models here.

class Contact(models.Model):
	chinesename = models.CharField(max_length=20)
	englishname = models.CharField(max_length=20)
	schoolid = models.CharField(max_length=20)
	department = models.CharField(max_length=30)
	introduction = models.CharField(max_length=200)
	selfie = models.FileField(upload_to='static/selfies')
	
	def __unicode__(self):
		return self.chinesename

	def __str__(self):
		return self.chinesename
	
	def contact_selfie(self):
		return '<img src="/%s" height="50" width="50"/>' % self.selfie
	contact_selfie.allow_tags = True