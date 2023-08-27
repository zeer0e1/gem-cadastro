from django.shortcuts import render, redirect, get_object_or_404
from aluno.forms import AlunoForm
from django.urls import reverse
from aluno.models import Aluno
from django.contrib.auth.decorators import login_required


@login_required(login_url='aluno:login')
def create(request):

    form_action = reverse('aluno:create')

    if request.method == 'POST':
        form = AlunoForm(request.POST)

        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            aluno = form.save()
            return redirect('aluno:update', aluno_id=aluno.pk)

        return render(request,
                      'aluno/create.html',
                      context)

    context = {
        'form': AlunoForm(),
        'form_action': form_action
    }

    return render(request,
                  'aluno/create.html',
                  context
                  )


@login_required(login_url='aluno:login')
def update(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk=aluno_id)
    form_action = reverse('aluno:update', args=(aluno_id,))
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)

        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            aluno = form.save()
            return redirect('aluno:update', aluno_id=aluno.pk)

        return render(request,
                      'aluno/create.html',
                      context)

    context = {
        'form': AlunoForm(instance=aluno),
        'form_action': form_action
    }

    return render(request,
                  'aluno/create.html',
                  context
                  )


@login_required(login_url='aluno:login')
def delete(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk=aluno_id)

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        aluno.delete()
        return redirect('aluno:index')

    return render(
        request,
        'aluno/aluno.html',
        {
            'aluno': aluno,
            'confirmation': confirmation,
        }
    )
