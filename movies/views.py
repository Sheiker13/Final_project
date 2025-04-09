
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm
from .models import Movie

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def index(request):
    return render(request, 'index.html')

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'catalog.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movie_detail.html', {'movie': movie})
