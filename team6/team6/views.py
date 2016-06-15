#from django.http import HttpResponse
from django.shortcuts import render_to_response
from recipe.models import Menu, Recipe, Ingrediant, Step, Comment
from recipe.models import Contact

#def here(request):
#	return HttpResponse('Mom, I am here!')

def index(reuqest):
	menu = Menu.objects.all()
	return render_to_response('index.html', locals())

def comment(request, id):
	if id:
		r = Recipe.objects.get(id=id)
	else:
		return HttpResponseRedirect("/recipe/")

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
	return render_to_response('recipe.html', locals())

