from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class CustomUser(AbstractUser):
    is_moderator = models.BooleanField(default=False)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Genre(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name


class Movie(BaseModel):
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    release_date = models.DateField()
    image = models.ImageField(upload_to='movies/', null=True, blank=True)
    genres = models.ManyToManyField(Genre, related_name='movies')

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
        ordering = ['-release_date']

    def __str__(self):
        return self.title


class Review(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ['-created_at']
        unique_together = ('user', 'movie')

    def __str__(self):
        return f"Review by {self.user.username} on {self.movie.title}"


class Rating(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    score = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"
        unique_together = ('user', 'movie')

    def __str__(self):
        return f"{self.score} - {self.movie.title} by {self.user.username}"


class FavoriteMovie(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Favorite Movie"
        verbose_name_plural = "Favorite Movies"
        unique_together = ('user', 'movie')

    def __str__(self):
        return f"{self.user.username} likes {self.movie.title}"


class UserMovieList(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movie, related_name='user_lists')

    class Meta:
        verbose_name = "User Movie List"
        verbose_name_plural = "User Movie Lists"
        unique_together = ('user', 'name')

    def __str__(self):
        return f"{self.name} by {self.user.username}"
