from django.db import models
from subgenres.models import Subgenre


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    subgenres = models.ManyToManyField(Subgenre, related_name="genres", verbose_name="Subgêneros")

    class Meta:
        verbose_name = 'Gênero'

    def __str__(self):
        return self.name
