from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/', include('movies.urls')),
    path('api/', include('movies.api_urls')),
<<<<<<< HEAD
    path('', include('movies.urls')),
=======
    path('', lambda request: redirect('movie_list'), name='index'),
>>>>>>> e25a141 (Улучшил интерфейс)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
