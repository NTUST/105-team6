from django.contrib import admin
from recipe.models import Menu, Recipe, Ingrediant, Step, Image, Comment
from recipe.models import Contact
# Register your models here.

class MenuAdmin(admin.ModelAdmin):
	list_display = ('name',)

class RecipeAdmin(admin.ModelAdmin):
	list_display = ('menu','name', 'introduction', 'admin_ingrediants', 'admin_steps', 'admin_images')
	list_filter = ('menu',)

class IngrediantAdmin(admin.ModelAdmin):
	list_display = ('recipe', 'index', 'food', 'amount')
	list_filter = ('recipe',)

class StepAdmin(admin.ModelAdmin):
	list_display = ('recipe', 'index', 'content')
	list_filter = ('recipe',)

class ImageAdmin(admin.ModelAdmin):
	list_display = ('recipe', 'index', 'admin_image')
	list_filter = ('recipe',)

class ReplyComment(admin.ModelAdmin):
	list_display = ('recipe', 'visitor', 'date_time', 'content', 'reply')
	list_filter = ('recipe',)

class ContactAdmin(admin.ModelAdmin):
	list_display = ('chinesename', 'englishname', 'schoolid', 'department', 'introduction')
	list_filter = ('chinesename',)
#'selfie'

admin.site.register(Menu, MenuAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingrediant, IngrediantAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Comment, ReplyComment)
admin.site.register(Contact, ContactAdmin)
