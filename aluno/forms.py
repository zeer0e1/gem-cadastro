from django.core.exceptions import ValidationError
from aluno.models import Aluno
from django import forms


class AlunoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Aluno
        fields = (
            'nome_completo',
            'localidade',
            'instrumento',
            'estado_civil',
            'telefone',
            'operadora',
            'date_nascimento',
            'data_batismo',
            'inicio_gem',
        )

        widgets = {
            'date_nascimento': forms.TextInput(attrs={'type': 'date'}),
            'data_batismo': forms.TextInput(attrs={'type': 'date'}),
            'inicio_gem': forms.TextInput(attrs={'type': 'date'}),
        }

    def clean(self):

        return super().clean()
