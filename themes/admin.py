from django.contrib import admin
from .models import Theme


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
