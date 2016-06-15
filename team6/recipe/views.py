from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone		#for date_time

from recipe.models import Menu, Recipe, Ingrediant, Step, Comment

# Create your views here.

def recipe(request, recipe_s):
	menu = Menu.objects.all()
	recipe = Recipe.objects.get(name=recipe_s)
	errors = []
	if request.POST:
		visitor = request.POST['visitor']
		content = request.POST['content']
		private = request.POST['private']
		date_time = timezone.localtime(timezone.now())
		if any(not request.POST[k] for k in request.POST):
			errors.append('* 有空白欄位，請不要留空')
		if not errors:
			Comment.objects.create(
				visitor=visitor,
				content=content,
				date_time=date_time,
				private=private,
				recipe=recipe
			)
			visistor, content = ('', '')

	return render_to_response('recipe.html', RequestContext(request, locals()))