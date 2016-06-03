from django.db import models

# Create your models here.
class Menu(models.Model):
	name = models.CharField(max_length=20)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

class Recipe(models.Model):
	menu = models.ForeignKey(Menu)
	name = models.CharField(max_length=20)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

class Ingrediant(models.Model):
	recipe = models.ForeignKey(Recipe)
	index = models.DecimalField(max_digits=2,decimal_places=0)
	food = models.CharField(max_length=20)
	amount = models.CharField(max_length=20)

class Step(models.Model):
	recipe = models.ForeignKey(Recipe)
	index = models.DecimalField(max_digits=2,decimal_places=0)
	content = models.CharField(max_length=200)

class Image(models.Model):
	recipe = models.ForeignKey(Recipe)
	index = models.DecimalField(max_digits=2,decimal_places=0)
	image = models.FileField(upload_to='static/images')

	def admin_image(self):
		return '<img src="/%s" height="50" width="50"/>' % self.image
	admin_image.allow_tags = True
	
