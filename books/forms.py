from django import forms
from genres.models import Genre
from subgenres.models import Subgenre
from themes.models import Theme
from .models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'

    def clean_subgenre(self):
        subgenre_name = self.cleaned_data.get('subgenre')
        genre_name = self.cleaned_data.get('genre')
        if genre_name and subgenre_name:
            try:
                genre = Genre.objects.get(name=genre_name)
                allowed_subgenres = genre.subgenres.all()
                subgenre = Subgenre.objects.get(name=subgenre_name)
                if subgenre not in allowed_subgenres:
                    self.add_error("subgenre", f"O subgênero {subgenre} não está incluso em {genre}")
            except (Genre.DoesNotExist, Subgenre.DoesNotExist) as e:
                self.add_error("subgenre", f"Algum objeto selecionado não existe: {e}")
            return subgenre

    def clean_themes(self):
        themes = self.cleaned_data.get('themes')
        subgenre_name = self.cleaned_data.get('subgenre')
        if subgenre_name and themes:
            try:
                subgenre = Subgenre.objects.get(name=subgenre_name)
                themes_ids_prompted = [theme.id for theme in themes]
                allowed_themes_ids = [theme.id for theme in subgenre.themes.all()]
                invalid_themes = [Theme.objects.get(id=theme_id) for theme_id in themes_ids_prompted if theme_id not in allowed_themes_ids]
                if invalid_themes:
                    self.add_error("themes", f"Os seguintes temas não são válidos para o subgênero {subgenre}: "
                                   f"{", ".join(map(str, invalid_themes))}")
            except (Subgenre.DoesNotExist, Theme.DoesNotExist) as e:
                self.add_error("themes", f"Algum objeto selecionado não existe: {e}")
            return themes
