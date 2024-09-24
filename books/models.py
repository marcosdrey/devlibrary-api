from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator
from django.contrib.auth.models import User
from genres.models import Genre
from subgenres.models import Subgenre
from publishers.models import Publisher
from authors.models import Author
from themes.models import Theme
from .validators import MaxDateValidator
from datetime import datetime


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(null=True, blank=True, verbose_name="Descrição", validators=[
        MinLengthValidator(3, "A descrição deve ter, no mínimo, 3 caracteres."),
        MaxLengthValidator(1000, "A descrição do livro não pode ultrapassar 1000 caracteres.")
    ])
    photo = models.ImageField(upload_to="book-photos", verbose_name="Foto")
    genre = models.ForeignKey(Genre,
                              on_delete=models.PROTECT,
                              related_name="books",
                              verbose_name="Gênero")
    subgenre = models.ForeignKey(Subgenre,
                                 on_delete=models.PROTECT,
                                 related_name="books",
                                 verbose_name="Subgênero")
    publisher = models.ForeignKey(Publisher,
                                  on_delete=models.PROTECT,
                                  related_name="books",
                                  verbose_name="Editora",
                                  null=True,
                                  blank=True)
    authors = models.ManyToManyField(Author,
                                     related_name="books",
                                     verbose_name="Autores")
    release_date = models.DateField(verbose_name="Data de Lançamento",
                                    validators=[
                                        MaxDateValidator(datetime.now(),
                                                         "A data não pode ser maior do que a atual.")])
    themes = models.ManyToManyField(Theme, related_name='books', verbose_name="Temas")

    class Meta:
        verbose_name = "Livro"

    def __str__(self):
        return self.title


class BookReview(models.Model):
    rating = models.IntegerField(validators=[
        MinValueValidator(0, "O valor mínimo de avaliação é 0."),
        MaxValueValidator(5, "O valor máximo de avaliação é 5.")
    ], verbose_name="Avaliação")
    comment = models.TextField(verbose_name="Comentário", validators=[
        MinLengthValidator(3, "Comentário deve ter, no mínimo, 3 caracteres."),
        MaxLengthValidator(500, "Comentário não pode ter mais de 500 caracteres.")
    ], null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="book_reviews", verbose_name="Usuário")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews", verbose_name="Livro")
    created_at = models.DateField(auto_now_add=True, verbose_name="Criado em")
    likes = models.ManyToManyField(User, blank=True, related_name="liked_comments", verbose_name="Curtidas")

    class Meta:
        verbose_name = "Avaliação"
        constraints = [
            models.UniqueConstraint(fields=['user', 'book'], name='unique_user_book_review')
        ]
        ordering = ['-created_at']

    def __str__(self):
        return f"'{self.user}' em '{self.book}'"
