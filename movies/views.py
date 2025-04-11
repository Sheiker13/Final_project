from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Avg, Q
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.http import JsonResponse
import json

from .models import Movie, Genre, FavoriteMovie, Review, Rating
from .forms import RegisterForm, ReviewForm, RatingForm, CustomUserCreationForm

# ----- Регистрация через FBV -----
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

# ----- Регистрация через CBV -----
class RegisterView(FormView):
    template_name = "registration/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# ----- Главная -----
def index(request):
    top_movies = Movie.objects.annotate(avg_rating=Avg('ratings__score')).order_by('-avg_rating')[:10]
    new_movies = Movie.objects.order_by('-release_date')[:10]
    popular_movies = Movie.objects.annotate(review_count=Count('reviews')).order_by('-review_count')[:10]

    return render(request, 'index.html', {
        'top_movies': top_movies,
        'new_movies': new_movies,
        'popular_movies': popular_movies,
    })

# ----- Каталог -----
def catalog_view(request):
    query = request.GET.get("q", "")
    genre_id = request.GET.get("genre")
    sort = request.GET.get("sort", "-release_date")

    movies = Movie.objects.all().annotate(average_rating=Avg("ratings__score"))

    if genre_id:
        movies = movies.filter(genres__id=genre_id)

    if query:
        movies = movies.filter(Q(title__icontains=query) | Q(description__icontains=query))

    if sort:
        movies = movies.order_by(sort)

    favorites = []
    if request.user.is_authenticated:
        favorites = request.user.favoritemovie_set.values_list("movie_id", flat=True)

    return render(request, "catalog.html", {
        "movies": movies,
        "search_query": query,
        "genres": Genre.objects.all(),
        "selected_genre": genre_id,
        "selected_sort": sort,
        "favorites": favorites,
    })

# ----- movie_list -----
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'catalog.html', {'movies': movies})

# ----- Детальная страница -----
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    average_rating = movie.ratings.aggregate(avg=Avg('score'))['avg']
    is_favorite = False

    if request.user.is_authenticated:
        is_favorite = FavoriteMovie.objects.filter(user=request.user, movie=movie).exists()

        # --- Обработка формы оценки ---
        if request.method == "POST" and "score" in request.POST:
            rating_form = RatingForm(request.POST)
            if rating_form.is_valid():
                score = rating_form.cleaned_data["score"]
                Rating.objects.update_or_create(
                    user=request.user,
                    movie=movie,
                    defaults={"score": score}
                )
                return redirect("movie_detail", pk=pk)
        else:
            try:
                existing = Rating.objects.get(user=request.user, movie=movie)
                rating_form = RatingForm(initial={"score": existing.score})
            except Rating.DoesNotExist:
                rating_form = RatingForm()

        # --- Обработка формы отзыва ---
        if request.method == "POST" and "text" in request.POST:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.user = request.user
                review.movie = movie
                review.save()
                return redirect("movie_detail", pk=pk)
        else:
            review_form = ReviewForm()

        # --- Обработка избранного (через скрытое поле) ---
        if request.method == "POST" and "toggle_fav" in request.POST:
            fav, created = FavoriteMovie.objects.get_or_create(user=request.user, movie=movie)
            if not created:
                fav.delete()
            return redirect("movie_detail", pk=pk)
    else:
        rating_form = RatingForm()
        review_form = ReviewForm()

    return render(request, 'movie_detail_dev.html', {
        'movie': movie,
        'form': review_form,
        'rating_form': rating_form,
        'average_rating': average_rating,
        'is_favorite': is_favorite,
    })


# ----- Профиль -----
@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})

# ----- Добавить отзыв -----
@login_required
def add_review(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()
    return redirect('movie_detail', pk=pk)

# ----- Оценить фильм (AJAX) -----
@csrf_exempt
@login_required
def rate_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        data = json.loads(request.body)
        score = int(data.get("score"))
        Rating.objects.update_or_create(user=request.user, movie=movie, defaults={"score": score})
        new_avg = movie.ratings.aggregate(avg=Avg("score"))["avg"]
        return JsonResponse({"success": True, "new_avg": round(new_avg or 0, 1)})
    return redirect("movie_detail", pk=pk)

# ----- Избранное: toggle (AJAX + обычный POST) -----
@login_required
def toggle_favorite(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    favorite, created = FavoriteMovie.objects.get_or_create(user=request.user, movie=movie)

    if not created:
        favorite.delete()
        is_favorite = False
    else:
        is_favorite = True

    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return JsonResponse({'is_favorite': is_favorite})

    return redirect(request.META.get("HTTP_REFERER", reverse_lazy("movie_detail", kwargs={'pk': pk})))
