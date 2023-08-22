from django.contrib import admin
from cadastro import models


@admin.register(models.Cadastro)
class Cadastro_admin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome_completo',
        'localidade',
        'telefone',
    )
    ordering = ('-id',)
    list_filter = ('id',)
    search_fields = ('id', 'nome_completo', 'localidade',)
    list_per_page = 1
    list_max_show_all = 100
    list_editable = ('nome_completo', 'telefone',)
    list_display_links = ('id', 'localidade',)
