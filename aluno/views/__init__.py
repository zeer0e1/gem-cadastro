from django.shortcuts import render
from aluno.models import Aluno


def index(request):
    alunos = Aluno.objects

    context = {
        'alunos': alunos,
    }

    return render(
        request,
        'aluno/site/index.html',
        context
    )
# Create your views here.
