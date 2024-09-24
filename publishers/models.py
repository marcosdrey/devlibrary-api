from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Publisher(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(max_length=200, verbose_name="Email", unique=True)
    phone_number = PhoneNumberField(verbose_name="Número de Telefone", unique=True)

    class Meta:
        verbose_name = 'Editora'

    def __str__(self):
        return self.name
