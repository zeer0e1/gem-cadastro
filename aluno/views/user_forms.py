from django.shortcuts import render, redirect
from aluno.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def register(request):
    form = RegisterForm

    messages.info(request, 'Um texto qualquer')
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario Registrado')
            return redirect('aluno:dashboard')

    return render(
        request,
        'aluno/register.html',
        {
            'form': form
        }
    )


@login_required(login_url='aluno:login')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(
            request,
            'aluno/register.html',
            {
                'form': form
            }
        )

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'aluno/register.html',
            {
                'form': form
            }
        )

    form.save()

    return redirect('aluno:logout')


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('aluno:dashboard')
        messages.error(request, 'Login inválido')

    return render(
        request,
        'aluno/login.html',
        {
            'form': form
        }
    )


@login_required(login_url='aluno:login')
def logout_view(request):
    auth.logout(request)
    return redirect('aluno:login')
