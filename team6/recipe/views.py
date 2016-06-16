from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone		#for date_time

from recipe.models import Menu, Recipe, Ingrediant, Step, Comment, Contact

# Create your views here.

def index(reuqest):
	menu = Menu.objects.all()
	return render_to_response('index.html', locals())

def recipe(request, recipe_s):
	menu = Menu.objects.all()
	recipe = Recipe.objects.get(name=recipe_s)
	errors = []
	if request.POST:
		visitor = request.POST['visitor']
		content = request.POST['content']
		getprivate = request.POST['private']
		if getprivate == "true":
			private = True
		else:
			private = False
		date_time = timezone.localtime(timezone.now())
		if any(not request.POST[k] for k in request.POST):
			errors.append("* 尚有表格未完成填寫！")
		if not errors:
			Comment.objects.create(
				visitor=visitor,
				content=content,
				private=private,
				date_time=date_time,
				recipe=recipe
			)
			visitor, content = ('', '')

	return render_to_response('recipe.html', RequestContext(request, locals()))

def contact(request):
	menu = Menu.objects.all()
	contact = Contact.objects.all()
	#cn = chinesename.objects.all()
	#en = englishname.objects.all()
	#si = schoolid.objects.all()
	#dp = department.objects.all()
	#it = introduction.objects.all()
	return render_to_response('contact.html', locals()) 