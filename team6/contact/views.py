from django.shortcuts import render_to_response

from recipe.models import Menu
from contact.models import Contact
# Create your views here.

def contact(request):
	menu = Menu.objects.all()
	contact = Contact.objects.all()
	
	return render_to_response('contact.html', locals()) 