from django.urls import path
from . import views
from .views import (
    register,
    RegisterView,
    catalog_view,
)

urlpatterns = [
    path('accounts/register/', register, name='register'),
    path('', views.index, name='index'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('catalog/', catalog_view, name='catalog'),
]
