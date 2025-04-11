from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    RegisterView,
    catalog_view,
    register
)

urlpatterns = [
    path('accounts/register/', register, name='register'),
    path('', views.index, name='index'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('catalog/', catalog_view, name='catalog'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('movies/<int:pk>/review/', views.add_review, name='add_review'),
    path('movies/<int:pk>/rate/', views.rate_movie, name='rate_movie'),
    path('movies/<int:pk>/favorite/', views.toggle_favorite, name='toggle_favorite'),
]
