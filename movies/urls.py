from django.urls import path
from . import views
from .views import register

urlpatterns = [
    path('accounts/register/', register, name='register'),
    path('', views.index, name='index'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:pk>/', views.movie_detail, name='movie_detail'),
]
