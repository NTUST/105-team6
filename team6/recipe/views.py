from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

from recipe.models import Menu, Recipe, Ingrediant, Step, Comment

# Create your views here.

def recipe(request, recipe_s):
	menu = Menu.objects.all()
	recipe = Recipe.objects.get(name=recipe_s)
	return render_to_response('recipe.html', locals())	

def comment(request, recipe_s):
	r = Recipe.objects.get(name=recipe_s)

	if request.POST:
			visitor = request.POST['visitor']
			content = request.POST['content']
			date_time = timezone.localtime(timezone.now())
			Comment.objects.create(
				visitor=visitor,
				content=content,
				date_time=date_time,
				recipe=r
			)
	return render_to_response('recipe.html', RequestContext(request, locals()))