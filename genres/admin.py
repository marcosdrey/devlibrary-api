from django.contrib import admin
from .models import Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'show_subgenres')
    search_fields = ('name',)

    def show_subgenres(self, obj):
        return ', '.join(str(subgenre) for subgenre in obj.subgenres.all())

    show_subgenres.short_description = 'Subgêneros'
