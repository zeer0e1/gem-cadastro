from django.shortcuts import render
from aluno.models import Aluno


def index(request):
    alunos = Aluno.objects \
        .filter(show=True)\
        .order_by('-id')

    context = {
        'alunos': alunos,
    }

    return render(
        request,
        'aluno/index.html',
        context
    )


def about(request):

    alunos = Aluno.objects

    context = {
        'alunos': alunos
    }

    return render(
        request,
        'aluno/about-us.html',
        context

    )
# Create your views here.
