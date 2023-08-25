from django.shortcuts import render, get_object_or_404, redirect
from aluno.models import Aluno
from django.db.models import Q
from django.core.paginator import Paginator
from django.db.models import Count

# -------------------------------------------------
import json


def index(request):

    alunos_por_instrumento = Aluno.objects.values(
        'instrumento__nome').annotate(quantidade_alunos=Count('id'))

    alunos_por_localidade = Aluno.objects.values(
        'localidade__localidade').annotate(quantidades=Count('id')

                                           )
    serialized_data = [
        {
            'label': resultado['instrumento__nome'],
            'y': resultado['quantidade_alunos']
        }
        for resultado in alunos_por_instrumento
    ]

    serialized_data2 = [
        {
            'label': resultado['localidade__localidade'],
            'y': resultado['quantidades']
        }
        for resultado in alunos_por_localidade
    ]

    context = {
        'site_title': 'Alunos'
    }

    return render(request,
                  'aluno/site/index.html',
                  {'context': context,
                   "alunosPorInstrumento": json.dumps(serialized_data),
                   "alunosPorLocalidade": json.dumps(serialized_data2)
                   })


def about(request):
    alunos = Aluno.objects.all() \
        .order_by('-id')

    paginator = Paginator(alunos, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Alunos'
    }
    return render(
        request,
        'aluno/site/about-us.html',
        context

    )


def search(request):
    search_value = request.GET.get('q').strip()

    if search_value == '':
        return redirect('aluno:about-us')

    alunos = Aluno.objects.all() \
        .filter(
        Q(nome_completo__icontains=search_value) |
        Q(instrumento__nome__icontains=search_value) |
        Q(localidade__icontains=search_value)
    )\
        .order_by('-id')

    paginator = Paginator(alunos, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Alunos'
    }
    return render(
        request,
        'aluno/site/about-us.html',
        context

    )


def aluno(request, aluno_id):

    # single_aluno = Aluno.objects.filter(pk=aluno_id).last()
    single_aluno = get_object_or_404(Aluno, pk=aluno_id)

    context = {
        'aluno': single_aluno,
        'site_title': 'Aluno'
    }
    return render(
        request,
        'aluno/aluno.html',
        context

    )
