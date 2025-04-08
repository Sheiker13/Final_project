from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Genre, Review
from .forms import ReviewForm

def index(request):
    return render(request, 'index.html')

def movie_list(request):
    genre_id = request.GET.get("genre")
    year = request.GET.get("year")

    movies = Movie.objects.all()

    if genre_id:
        movies = movies.filter(genres__id=genre_id)

    if year:
        movies = movies.filter(release_date__year=year)

    genres = Genre.objects.all()
    years = Movie.objects.dates("release_date", "year")

    return render(request, 'catalog.html', {
        'movies': movies,
        'genres': genres,
        'years': years,
        'selected_genre': genre_id,
        'selected_year': year,
    })

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    form = ReviewForm()

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
            return redirect('movie_detail', pk=pk)

    return render(request, 'movie_detail.html', {
        'movie': movie,
        'form': form,
    })

from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterForm

from django.contrib.auth import login
from django.shortcuts import redirect

class RegisterView(CreateView):
    template_name = "registration/register.html"
    form_class = RegisterForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("movie_list")