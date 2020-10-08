from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Player
from .forms import StatsForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def players_index(request):
    players = Player.objects.all()
    return render(request, 'players/index.html', {'players': players})


def players_detail(request, player_id):
    player = Player.objects.get(id=player_id)
    stats_form = StatsForm()
    return render(request, 'players/detail.html', {'player': player, 'stats_form': stats_form})


def add_stats(request, player_id):
    form = StatsForm(request.POST)
    if form.is_valid():
        new_stats = form.save(commit=False)
        new_stats.player_id = player_id
        new_stats.save()
    return redirect('detail', player_id=player_id)


class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'
    success_url = '/players/'


class PlayerUpdate(UpdateView):
    model = Player
    fields = '__all__'


class PlayerDelete(DeleteView):
    model = Player
    success_url = '/players/'
