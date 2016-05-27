from django.http import HttpResponse
from django.shortcuts import render_to_response

def here(request):
	return HttpResponse('Mom, I am here!')

def recipe(request):
	return render_to_response('recipe.html', locals())	
