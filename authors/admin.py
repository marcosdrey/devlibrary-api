from django.contrib import admin
from .models import Nationality, Author


@admin.register(Nationality)
class NationalityAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_qt_authors')
    search_fields = ('name',)

    def show_qt_authors(self, obj):
        return len(obj.authors.all())

    show_qt_authors.short_description = 'Qtd. de Autores'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality')
    search_fields = ('name',)
