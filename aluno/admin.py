from django.contrib import admin
from aluno import models


@admin.register(models.Aluno)
class Aluno_admin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome_completo',
        'localidade',
        'telefone',
        'instrumento',
    )
    ordering = ('-id',)
    #list_filter = ('id',)
    search_fields = ('id', 'nome_completo', 'localidade','instrumento',)
    list_per_page = 10
    list_max_show_all = 100
    list_editable = ('nome_completo', 'telefone',)
    list_display_links = ('id', 'localidade',)
    

@admin.register(models.Instrumento)
class Instrumento_admin(admin.ModelAdmin):
    list_display = (
        'nome',
    )
    ordering = ('-id',)
