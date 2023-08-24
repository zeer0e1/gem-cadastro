from django.shortcuts import render, get_object_or_404, redirect
from aluno.models import Aluno
from django.db.models import Q
from django.core.paginator import Paginator
# -------------------------------------------------


def index(request):
    data_points = [
        {"label": "apple",  "y": 10},
        {"label": "orange", "y": 15},
        {"label": "banana", "y": 25},
        {"label": "mango",  "y": 30},
        {"label": "grape",  "y": 28}
    ]
    return render(request, 'aluno/site/index.html', {"data_points": data_points})


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
