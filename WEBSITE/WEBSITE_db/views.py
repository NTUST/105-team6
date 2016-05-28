from django.shortcuts import render
from WEBSITE_db.models import Recipe, Comment

def recipe(request):
	recipe = Recipe.objects.all()
	comment = Comment.objects.all()
	return render_to_response('recipe.html',locals())