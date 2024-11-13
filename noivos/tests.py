from django.test import TestCase
from noivos.models import Convidados
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import datetime

class TesteConvidado(TestCase):

    def test_cadastroData(self):

        convidado = Convidados(nome_convidado = 'Convidado 10',
                    whatsapp = '217654',
                    status='C',
                    data_status = timezone.make_aware(datetime.now()))

        convidado.save()
        print(convidado)
        print(convidado.data_status)
        
