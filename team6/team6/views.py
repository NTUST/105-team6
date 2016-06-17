# -*- coding: utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render_to_response
from recipe.models import Menu, Recipe, Ingrediant, Step, Comment
from recipe.models import Contact

#def here(request):
#	return HttpResponse('Mom, I am here!')

def index(reuqest):
	menu = Menu.objects.all()
	return render_to_response('index.html', locals())