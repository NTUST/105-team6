from django.contrib import admin
from recipe.models import Menu, Recipe, Ingrediant, Step, Image
# Register your models here.

class MenuAdmin(admin.ModelAdmin):
	list_display = ('name',)

class RecipeAdmin(admin.ModelAdmin):
	list_display = ('menu','name', 'admin_ingrediants', 'admin_steps', 'admin_images')
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

admin.site.register(Menu, MenuAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingrediant, IngrediantAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(Image, ImageAdmin)
