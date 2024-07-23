from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe

def main_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'main.html', {'recipes': recipes})

def Add_view(request):
    if request.method == 'POST':
        new_recipe = Recipe(
            name=request.POST.get('name'),
            ingredients=request.POST.get('ingredients'),
            instructions=request.POST.get('instructions'),
        )
        new_recipe.save()
        return redirect('main') 
    return render(request, 'add_recipe.html') 

def Edit_view(request, title):
    recipe = get_object_or_404(Recipe, name=title)

    if request.method == 'POST':
        recipe.name = request.POST.get('name')
        recipe.ingredients = request.POST.get('ingredients')
        recipe.instructions = request.POST.get('instructions')
        recipe.save()
        return redirect('main')
    
    return render(request, 'edit_recipe.html', {'recipe': recipe})

def Delete_view(request, title):
    recipe = get_object_or_404(Recipe, name=title)

    if request.method == 'POST':
        recipe.delete()
        return redirect('main') 

    return render(request, 'confirm_delete.html', {'recipe': recipe}) 
