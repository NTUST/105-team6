from django.db import models

#Create your models here.
class Recipe(models.Model):
	name = models.CharField(max_length=10)
	#ingrediants = models.CharField(max_length=15)
	#steps = models.CharField(max_length=50, blank=True)
	#picture1 = (for background picture)
	#picture2 = (for background picture)
	#picture3 = (for background picture)

class Comment(models.Model):
	recipe = models.ForeignKey(Recipe)
	name = models.CharField(max_length=20)
	private = models.BooleanField(default=False)
	contents = models.CharField(max_length=50, blank=True)