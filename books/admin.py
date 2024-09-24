from django.contrib import admin
from .forms import BookForm
from .models import Book, BookReview


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'show_authors', 'show_themes', 'publisher', 'release_date')
    search_fields = ('title', 'genre')
    form = BookForm

    def show_authors(self, obj):
        return ', '.join([str(author) for author in obj.authors.all()])

    def show_themes(self, obj):
        return ', '.join([str(theme) for theme in obj.themes.all()])

    show_authors.short_description = 'Autores'
    show_themes.short_description = 'Temas'


@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    list_display = ('rating', 'user', 'book', 'created_at', 'show_likes')
    search_fields = ('book',)

    def show_likes(self, obj):
        return obj.likes.count()

    show_likes.short_description = 'Curtidas'
