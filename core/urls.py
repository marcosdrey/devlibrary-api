from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('authentication.urls')),
    path('api/v1/genres/', include('genres.urls')),
    path('api/v1/subgenres/', include('subgenres.urls')),
    path('api/v1/themes/', include('themes.urls')),
    path('api/v1/publishers/', include('publishers.urls')),
    path('api/v1/authors/', include('authors.urls')),
    path('api/v1/books/', include('books.urls')),
    path('api/v1/users/', include('users.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
