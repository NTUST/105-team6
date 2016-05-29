from django.shortcuts import render
from django.shortcuts import render_to_response

from recipe.models import Menu, Recipe, Ingrediant, Step

# Create your views here.

def recipe(request, recipe_s):
	menu = Menu.objects.all()
	recipe = Recipe.objects.get(name=recipe_s)
	return render_to_response('recipe.html', locals())	
