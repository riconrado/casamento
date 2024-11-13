from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from . models import Presentes, Convidados

def home(request):

    if request.method == "GET":

        presentes = Presentes.objects.all()

        qtdNaoReservado = Presentes.objects.filter(reservado=False).count()
        qtdReservado = Presentes.objects.filter(reservado=True).count()
    
        return render(request, 'home.html', {'presentes': presentes, 'qtdReservado':qtdReservado, 'qtdNaoReservado':qtdNaoReservado})
    
    else:

        nome_presente = request.POST["nome_presente"]
        foto = request.FILES.get('foto')
        preco = request.POST["preco"]
        importancia = int(request.POST["importancia"])

        presentes = Presentes(
            nome_presente = nome_presente,
            foto = foto,
            preco = preco,
            importancia = importancia
        )

        presentes.save()


        presentes = Presentes.objects.all()
        qtdNaoReservado = Presentes.objects.filter(reservado=False).count()
        qtdReservado = Presentes.objects.filter(reservado=True).count()

        qtdNaoReservado = Presentes.objects.filter(reservado=False).count()
        qtdReservado = Presentes.objects.filter(reservado=True).count()
    
        return render(request, 'home.html', {'presentes': presentes, 'qtdReservado':qtdReservado, 'qtdNaoReservado':qtdNaoReservado})


def lista_convidados(request):

    if request.method == 'GET':
        convidados = Convidados.objects.all()

        cont=0
        for i in convidados:

            if len(i.nome_convidado) == 0:
                cont +=1
                i.nome_convidado =  f'Convidado {cont}'
                i.status = 'AC'
                i.save()

        
        return render(request, 'lista_convidados.html', {"convidados": convidados})
    elif request.method == 'POST':
        nome_convidado = request.POST.get('nome_convidado')
        whatsapp = request.POST.get('whatsapp')
        maximo_acompanhantes = int(request.POST.get('maximo_acompanhantes'))

        convidados = Convidados(
                    nome_convidado=nome_convidado,
                    whatsapp=whatsapp,
                    maximo_acompanhantes=maximo_acompanhantes
                    )
        
        convidados.save()

        return redirect('lista_convidados')
    
def excluir_presente(request, id):
    presente = Presentes.objects.get(id=id)
    presente.delete()
    
    return redirect('home')