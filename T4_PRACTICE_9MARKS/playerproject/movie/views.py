from django.shortcuts import render
from django.http import HttpResponse
#
from .models import Movie
from .models import Review
from django.shortcuts import get_object_or_404,redirect

def home(request):
    searchTerm=request.GET.get('searchMovie')
    if searchTerm:
        movies=Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies=Movie.objects.all()
    return render(request,'home.html',{'searchTerm':searchTerm,'movies':movies})

def about(request):
    return HttpResponse("<h1>Welcome to about Page</h1>")

def signup(request):
    email=request.GET.get('email')
    return render(request,'signup.html',{'email':email})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    review = Review.objects.filter(movie=movie)
    return render(request, 'detail.html', {'movie': movie, 'reviews': review})

def createreview(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET':
        return render(request, 'createreview.html', { 'movie': movie})
    else:
        try:
             myreview = request.POST.get('myreview')
             newReview=Review()
             newReview.text = myreview
             newReview.movie = movie
             newReview.user = request.user    
             newReview.save()
             return redirect('detail', newReview.movie.id)
        
        except ValueError:
            return render(request, 'createreview.html', {'error': 'Bad data passed in. Try again.'})
def updatereview(request, review_id):
     review = get_object_or_404(Review, pk=review_id, user=request.user)
     if request.method == 'GET':
          return render(request, 'updatereview.html', {'review': review})
     else:
         try:
            review.text = request.POST.get('myreview')
            review.save()
            return redirect('detail', review.movie.id)
         except ValueError:
            return render(request, 'updatereview.html', {'review': review, 'error': 'Bad data passed in. Try again.'})
def deletereview(request, review_id):
     review = get_object_or_404(Review, pk=review_id, user=request.user)
     review.delete() 
     return redirect('detail', review.movie.id)

from rest_framework import viewsets
from .models import Movie,Review
from .serializers import MovieSerializer,ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import isAdminOrReadOnly

class MovieViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    permission_classes=[IsAuthenticated,isAdminOrReadOnly]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[IsAuthenticated,isAdminOrReadOnly]
