from django.shortcuts import render, redirect, get_object_or_404 # Fixed here (404 instead of 400)
from .models import Recipe

# 1. Welcome Page View
def welcome_page(request):
    return render(request, 'welcome.html')

# 2. Home Page View with search functionality by First Field (name)
def home_page(request):
    query = request.GET.get('search', '').strip()
    if query:
        recipes = Recipe.objects.filter(name__icontains=query)
    else:
        recipes = Recipe.objects.all()
    
    return render(request, 'home.html', {'recipes': recipes, 'query': query})

# 3. Add Recipe View
def add_recipe(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        cooking_time = request.POST.get('cooking_time')
        
        Recipe.objects.create(name=name, category=category, cooking_time=cooking_time)
        return redirect('home')
        
    return render(request, 'recipe_form.html', {'action': 'Add New'})

# 4. Edit Recipe View
def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk) # Fixed here
    
    if request.method == 'POST':
        recipe.name = request.POST.get('name')
        recipe.category = request.POST.get('category')
        recipe.cooking_time = request.POST.get('cooking_time')
        recipe.save()
        return redirect('home')
        
    return render(request, 'recipe_form.html', {'recipe': recipe, 'action': 'Edit'})

# 5. Delete Recipe View
def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk) # Fixed here
    recipe.delete()
    return redirect('home')
