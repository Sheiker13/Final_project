
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
<<<<<<< HEAD
from .forms import RegisterForm
=======
from .forms import RegisterForm, ReviewForm, RatingForm
>>>>>>> e25a141 (Улучшил интерфейс)
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
<<<<<<< HEAD
    return render(request, 'movie_detail.html', {'movie': movie})
=======
    form = ReviewForm()
    rating_form = RatingForm()
    return render(request, 'movie_detail.html', {
        'movie': movie,
        'form': form,
        'rating_form': rating_form
    })
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movie_detail.html', {'movie': movie})


from django.views.generic.edit import FormView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

class RegisterView(FormView):
    template_name = "registration/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


from django.views.generic import ListView
from .models import Movie, Genre
from django.db.models import Avg
from django.shortcuts import render

def catalog_view(request):
    genre_id = request.GET.get("genre")
    sort = request.GET.get("sort", "-release_date")
    movies = Movie.objects.all().annotate(average_rating=Avg("ratings__score"))

    if genre_id:
        movies = movies.filter(genres__id=genre_id)

    if sort:
        movies = movies.order_by(sort)

    genres = Genre.objects.all()
    return render(request, "catalog.html", {
        "movies": movies,
        "genres": genres,
        "selected_genre": genre_id,
        "selected_sort": sort,
    })
>>>>>>> e25a141 (Улучшил интерфейс)
