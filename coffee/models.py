from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Cafe(models.Model):
    nome = models.CharField(max_length=100)
    produtor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Avaliacao(models.Model):
    cafe = models.ForeignKey(
        Cafe,
        on_delete=models.CASCADE,
        related_name="avaliacoes",
    )

    aroma = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    sabor = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    acidez = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    corpo = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    finalizacao = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    observacoes = models.TextField(blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    @property
    def media(self):
        return (
            self.aroma
            + self.sabor
            + self.acidez
            + self.corpo
            + self.finalizacao
        ) / 5

    def __str__(self):
        return f"{self.cafe.nome} - Média: {self.media:.1f}"