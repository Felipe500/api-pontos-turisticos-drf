from django.db import models
from app.atracoes.models import Atracao
from app.comentarios.models import Comentario
from app.avaliacoes.models import Avaliacao
from app.enderecos.models import Endereco


class DocIdentificacao(models.Model):
    description = models.CharField(max_length=100)


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(
        Endereco, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)
    doc_identificacao = models.OneToOneField(
        DocIdentificacao, on_delete=models.CASCADE, null=True, blank=True
    )

    @property
    def descricao_completa2(self):
        return '%s - %s' % (self.nome, self.descricao)

    def __str__(self):
        return self.nome
