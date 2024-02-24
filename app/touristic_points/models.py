from django.db import models
from app.atracoes.models import Atracao
from app.avaliacoes.models import Avaliacao
from app.enderecos.models import Endereco


class TouristSpot(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    attractions = models.ManyToManyField(Atracao)
    assessments = models.ManyToManyField(Avaliacao)
    address = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='tourist_spot', null=True, blank=True)
    approved = models.BooleanField(default=False)

    @property
    def description_complete(self):
        return f'{self.name} - {self.description[:18]}'

    def __str__(self):
        return self.name
