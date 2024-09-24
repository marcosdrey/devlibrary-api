from django.db import models


class Theme(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')

    class Meta:
        verbose_name = 'Tema'

    def __str__(self):
        return self.name
