from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone
from datetime import datetime
from noivos.models import Convidados, Presentes
from .models import Acompanhantes

def convidados(request):
    token = request.GET.get('token')
    # convidado = Convidados.objects.get(token=token)
    convidado = get_object_or_404(Convidados, token=token)
    presentes = Presentes.objects.filter(reservado=False)
    acompanhantes = Acompanhantes.objects.filter(convidado=convidado)

    # return render(request, 'convidados.html', {'convidado': convidado,'presentes': presentes, 'token':token})
    return render(request, 'convidados.html', {'convidado': convidado,'presentes': presentes,'acompanhantes': acompanhantes, 'token':token})


def responder_presenca(request):
    resposta = request.GET.get('resposta')
    token = request.GET.get('token')
    
    convidado = get_object_or_404(Convidados, token=token)
    convidado.status = resposta
    convidado.data_status = timezone.make_aware(datetime.now())
    
    convidado.save()

    return redirect(f'{reverse('convidados')}?token={token}')


def reservar_presente(request, id):
        
        presente = get_object_or_404(Presentes, id=id)
        token = request.GET.get('token')
        # convidado = Convidados.objects.get(token=token)
        convidado = get_object_or_404(Convidados, token=token)

        presente.reservado = True
        presente.reservado_por = convidado
        presente.save()

        return redirect(f'{reverse('convidados')}?token={token}')


def cadastrar_acompanhante(request):
     nome_acompanhante = request.POST.get('nome')
     token = request.POST.get('token')
    #  convidado = Convidados.objects.get(token=token)
     convidado = get_object_or_404(Convidados, token=token)
     presentes = Presentes.objects.filter(reservado=False)
     
     acompanhante_cadastro = Acompanhantes(nome_acompanhante=nome_acompanhante,
                                    convidado=convidado)
     
     acompanhante_cadastro.save()

     acompanhantes = Acompanhantes.objects.filter(convidado=convidado)
     
     return render(request, 'convidados.html', {'convidado': convidado,'presentes': presentes,'acompanhantes': acompanhantes, 'token':token})

def excluir_acompanhante(request, id):
    #  acompanhante = Acompanhantes.objects.get(id=id)
     acompanhante = get_object_or_404(Acompanhantes, id=id)
     acompanhante.delete()

     token = request.GET.get('token')

     return redirect(f'{reverse('convidados')}?token={token}')