from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie  
# Create your views here.

def home(request):
    search_term = request.GET.get('searchMovie') 
    if search_term:
        movies = Movie.objects.filter(title__icontains=search_term)
    else:
        movies = Movie.objects.all()
    return render(request,"home.html",{'searchTerm': search_term, 'movies': movies})
def about(request):
    return render(request,"about.html")
def signup(request):
    user_email = request.GET.get('email')
    return render(request, "signup.html", {'email': user_email})