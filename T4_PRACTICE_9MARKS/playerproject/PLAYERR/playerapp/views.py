from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Player
# Create your views here.
def home(request):
    search=request.GET.get('search')
    if search:
        players=Player.objects.filter(name__icontains=search)
    else:
        players=Player.objects.all()
    return render(request,"home.html",{'players':players})
def welcome(request):
    return render(request,'welcome.html')
def add_player(request):
    if request.method=='POST':
        name=request.POST.get('name')
        innings=request.POST.get('innings')
        runs=request.POST.get('runs')
        Player.objects.create(name=name,test_innings=innings,runs=runs)
        return redirect('/')
    return render(request,'add_player.html')

def edit_player(request,id):
    player=get_object_or_404(Player,id=id)
    if request.method=='POST':
        player.name=request.POST.get('name')
        player.test_innings=request.POST.get('innings')
        player.runs=request.POST.get('runs')
        player.save()
        return redirect('/')
    return render(request,'edit_player.html',{'player':player})

def delete_player(request,id):
    player=get_object_or_404(Player,id=id)
    player.delete()
    return redirect('/')

from rest_framework import viewsets
from . models import Player
from .serializers import PlayerSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset=Player.objects.all()
    serializer_class=PlayerSerializer