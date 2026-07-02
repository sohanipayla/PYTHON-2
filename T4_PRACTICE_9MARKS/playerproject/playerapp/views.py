from django.shortcuts import render, redirect, get_object_or_404
from .models import Player

# 1. Home Page
def home(request):
    search_query = request.GET.get('search', '')
    if search_query:
        players = Player.objects.filter(name__icontains=search_query)
    else:
        players = Player.objects.all()
        
    # Yahan se humne 'playerapp/' hata kar direct 'home.html' kar diya hai
    return render(request, 'home.html', {'players': players})

# 2. Welcome Page
def welcome(request):
    return render(request, 'welcome.html')

# 3. Add Player Page
def add_player(request):
    if request.method == "POST":
        name = request.POST.get('name')
        innings = request.POST.get('innings') 
        runs = request.POST.get('runs')
        Player.objects.create(name=name, test_innings=innings, runs=runs)
        return redirect('/') 
    return render(request, 'add_player.html')

# 4. Edit Player Page
def edit_player(request, id):
    player = get_object_or_404(Player, id=id)
    if request.method == "POST":
        player.name = request.POST.get('name')
        player.test_innings = request.POST.get('innings') 
        player.runs = request.POST.get('runs')
        player.save()
        return redirect('/') 
    return render(request, 'edit_player.html', {'player': player})

# 5. Delete Player Function
def delete_player(request, id):
    player = get_object_or_404(Player, id=id)
    player.delete()
    return redirect('/')
