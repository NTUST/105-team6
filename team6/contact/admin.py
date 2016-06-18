from django.contrib import admin
from contact.models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
	list_display = ('chinesename', 'englishname', 'schoolid', 'department', 'introduction', 'contact_selfie')
	list_filter = ('chinesename',)

admin.site.register(Contact, ContactAdmin)