from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Player, Training
from .forms import StatsForm


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


@login_required
def players_index(request):
    players = Player.objects.filter(user=request.user)
    return render(request, 'players/index.html', {'players': players})


@login_required
def players_detail(request, player_id):
    player = Player.objects.get(id=player_id)
    trainings_player_doesnt_have = Training.objects.exclude(
        id__in=player.trainings.all().values_list('id'))
    stats_form = StatsForm()
    return render(request, 'players/detail.html', {'player': player, 'stats_form': stats_form, 'trainings': trainings_player_doesnt_have})


@login_required
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

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PlayerUpdate(UpdateView):
    model = Player
    fields = '__all__'


class PlayerDelete(DeleteView):
    model = Player
    success_url = '/players/'


class TrainingList(ListView):
    model = Training


class TrainingDetail(DetailView):
    model = Training


class TrainingCreate(CreateView):
    model = Training
    fields = '__all__'


class TrainingUpdate(UpdateView):
    model = Training
    fields = ['training_type', 'date', 'duration', 'completed', ]


class TrainingDelete(DeleteView):
    model = Training
    success_url = '/trainings/'

# @login_required
def assoc_training(request, player_id, training_id):
    Player.objects.get(id=player_id).trainings.add(training_id)
    return redirect('detail', player_id=player_id)
