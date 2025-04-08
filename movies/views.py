
from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Genre, Review, Rating
from .forms import ReviewForm, RatingForm

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
    review_form = ReviewForm()
    rating_form = RatingForm()

    if request.method == "POST":
        if 'text' in request.POST:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.movie = movie
                review.user = request.user
                review.save()
                return redirect('movie_detail', pk=pk)

        if 'score' in request.POST:
            rating_form = RatingForm(request.POST)
            if rating_form.is_valid():
                Rating.objects.update_or_create(
                    user=request.user,
                    movie=movie,
                    defaults={'score': rating_form.cleaned_data['score']}
                )
                return redirect('movie_detail', pk=pk)

    return render(request, 'movie_detail.html', {
        'movie': movie,
        'form': review_form,
        'rating_form': rating_form,
    })

from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterForm
from django.contrib.auth import login

class RegisterView(CreateView):
    template_name = "registration/register.html"
    form_class = RegisterForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("movie_list")
