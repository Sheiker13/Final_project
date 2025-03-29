from django.shortcuts import render
from .models import Movie

def index(request):
    return render(request, 'index.html')

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'catalog.html', {'movies': movies})

def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'movie_detail.html', {'movie': movie})
