from django.shortcuts import render_to_response
from django.template import RequestContext

from recipe.models import Menu, Recipe, Ingrediant, Step, Comment
from recipe.models import Contact
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

def contact(request):
	contact = Contact.objects.all()
	#cn = chinesename.objects.all()
	#en = englishname.objects.all()
	#si = schoolid.objects.all()
	#dp = department.objects.all()
	#it = introduction.objects.all()
	return render_to_response('contact.html', locals()) 