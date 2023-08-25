from django.shortcuts import render, get_object_or_404, redirect
from aluno.models import Aluno
from django import forms

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = (
            'nome_completo',
        )

def create(request):
    if request.method == 'POST':
        context = {
        'form': AlunoForm(request.POST)
        }
        
        return render(request, 
                      'aluno/create.html',
                      context)
    
    context = {
        'form': AlunoForm()
        }

    return render(request, 
                      'aluno/create.html',
                      context
                      )
    

   
   