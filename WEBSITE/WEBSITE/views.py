from django.shortcuts import render_to_response

def recipe(request):
	#recipe1 = {'name':'食譜名稱', 'ingrediant':填入食材(還有份量)**注意：格式未定, 'steps':'填入步驟', 'picture1':??, 'picture2':??, 'picture3':??}
	#recipe2 = {'name':'食譜名稱', 'ingrediant':填入食材(還有份量)**注意：格式未定, 'steps':'填入步驟', 'picture1':??, 'picture2':??, 'picture3':??}
	#recipe3 = {'name':'食譜名稱', 'ingrediant':填入食材(還有份量)**注意：格式未定, 'steps':'填入步驟', 'picture1':??, 'picture2':??, 'picture3':??}
	#recipe4 = {'name':'食譜名稱', 'ingrediant':填入食材(還有份量)**注意：格式未定, 'steps':'填入步驟', 'picture1':??, 'picture2':??, 'picture3':??}
	#recipe5 = {'name':'食譜名稱', 'ingrediant':填入食材(還有份量)**注意：格式未定, 'steps':'填入步驟', 'picture1':??, 'picture2':??, 'picture3':??}
	#recipe6 = {'name':'食譜名稱', 'ingrediant':填入食材(還有份量)**注意：格式未定, 'steps':'填入步驟', 'picture1':??, 'picture2':??, 'picture3':??}
	#recipes = [recipe1, recipe2, recipe3, recipe4, recipe5, recipe6]
	return render_to_response('recipe.html', locals())

#def Comment(request):
