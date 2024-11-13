from django.db import models
from noivos.models import Convidados

class Acompanhantes(models.Model):
    nome_acompanhante = models.CharField(max_length=100, null=True, blank=True)
    convidado = models.ForeignKey(Convidados, null=False ,on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.nome_acompanhante
