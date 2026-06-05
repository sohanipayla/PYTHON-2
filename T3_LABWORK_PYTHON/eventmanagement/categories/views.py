from django.shortcuts import render
from .models import Category

def event_categories(request):
    
    categories = Category.objects.all().order_by('name')
    
    return render(request, 'categories/categories_list.html', {'categories': categories })
