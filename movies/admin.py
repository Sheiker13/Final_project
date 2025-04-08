
from django.contrib import admin
from .models import Movie, Review, Rating, Genre, CustomUser, FavoriteMovie, UserMovieList

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0

class RatingInline(admin.TabularInline):
    model = Rating
    extra = 0

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date')
    search_fields = ('title',)
    list_filter = ('release_date', 'genres')
    inlines = [ReviewInline, RatingInline]

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_superuser', 'is_moderator')
    list_filter = ('is_superuser', 'is_moderator')

admin.site.register(FavoriteMovie)
admin.site.register(UserMovieList)
