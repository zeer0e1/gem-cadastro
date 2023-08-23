from django.db import models

# Create your models here.


# campos para serem criados


# Tabela aluno ( model aluno)

# Nome completo - string
# Localidade - String
# Estado civil - string
# data nascimento - date
# data bastismo - date
# inicio das aulas  - date
# telefone
# operadora


# Tabela de endereços
# CEP - int
# Endereço - string
# n - int
# Bairro - string


# Tabela categoria

class Instrumento(models.Model):
    class Meta:
        verbose_name = 'Instrumento'
        verbose_name_plural = 'Instrumentos'
        
    
    nome = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.nome


class Aluno(models.Model):
    nome_completo = models.CharField(max_length=200)
    localidade = models.CharField(max_length=200)
    estado_civil = models.CharField(max_length=100)
    telefone = models.CharField(max_length=200)
    operadora = models.CharField(max_length=20)
    date_nascimento = models.DateField()
    data_batismo = models.DateField(blank=True,null=True)
    inicio_gem = models.DateField()
    instrumento = models.ForeignKey(Instrumento, 
                                    on_delete=models.DO_NOTHING,
                                    )

    def __str__(self) -> str:
        return f'{self.nome_completo}'
