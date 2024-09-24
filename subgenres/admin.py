from django.contrib import admin
from .models import Subgenre


@admin.register(Subgenre)
class SubgenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'show_themes')
    search_fields = ('name',)

    def show_themes(self, obj):
        return ', '.join([str(theme) for theme in obj.themes.all()])

    show_themes.short_description = 'Temas'
