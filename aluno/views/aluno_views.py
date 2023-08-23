from django.shortcuts import render, get_object_or_404, redirect
from aluno.models import Aluno
from django.db.models import Q


def index(request):
    alunos = Aluno.objects

    context = {
        'alunos': alunos,
        'site_title': 'Dashboard'
    }

    return render(
        request,
        'aluno/site/index.html',
        context
    )


def about(request):
    alunos = Aluno.objects.all() \
        .order_by('-id')[:10]

    context = {
        'alunos': alunos,
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

    context = {
        'alunos': alunos,
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
