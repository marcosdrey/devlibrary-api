from django.db import models
from themes.models import Theme
from .validators import MaxSizeValidator


ICON_MAX_BYTES = 1024 * 1024  # 1MB


class Subgenre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    themes = models.ManyToManyField(Theme, related_name="subgenres", verbose_name="Temas")
    icon = models.ImageField(upload_to="subgenre-icons",
                             verbose_name="Ícone",
                             null=True,
                             blank=True,
                             validators=[
                                 MaxSizeValidator(ICON_MAX_BYTES,
                                                  "A imagem não pode ter mais de 1MB.")
                             ])

    class Meta:
        verbose_name = 'Subgênero'

    def __str__(self):
        return self.name
