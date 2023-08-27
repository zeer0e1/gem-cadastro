from django.core.exceptions import ValidationError
from aluno.models import Aluno
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation


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


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.',
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.'
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use the same password as before.',
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas não batem')
                )

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Já existe este e-mail', code='invalid')
                )

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(errors)
                )

        return password1


class RegisterUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )
