from django.db import models


class Nationality(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")

    class Meta:
        ordering = ['name']
        verbose_name = 'Nacionalidade'

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nome")
    nationality = models.ForeignKey(Nationality,
                                    on_delete=models.PROTECT,
                                    related_name='authors',
                                    verbose_name='Nacionalidade')

    class Meta:
        verbose_name = 'Autor'

    def __str__(self):
        return self.name
