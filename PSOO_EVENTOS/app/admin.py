from django.contrib import admin
from .models import *

class AtividadeInline(admin.TabularInline):
    model = Atividade
    extra = 1

class InscricaoInline(admin.TabularInline):
    model = Inscricao
    extra = 1

class PessoaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'telefone', 'email']
    search_fields = ['nome', 'email']

class AtividadeAdmin(admin.ModelAdmin):
    list_display = ['id', 'descricao', 'data_inicio', 'hora_inicio', 'data_fim', 'hora_fim', 'evento']
    search_fields = ['descricao']
    list_filter = ['evento']

class InscricaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'estado', 'evento', 'participante']
    search_fields = ['estado', 'participante__nome']
    list_filter = ['estado', 'evento']

class LocalAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'referencia']
    search_fields = ['nome']


class EventoAdmin(admin.ModelAdmin):
    list_display = ['id', 'descricao', 'data_inicio', 'hora_inicio', 'data_fim', 'hora_fim', 'local', 'categoria']
    search_fields = ['descricao']
    list_filter = ['categoria', 'local']
    inlines = [AtividadeInline, InscricaoInline]

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'avaliacao', 'palestrante', 'duracao', 'evento']
    search_fields = ['avaliacao', 'palestrante']
    list_filter = ['evento']

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']

admin.site.register(Atividade)
admin.site.register(Inscricao)
admin.site.register(Local)
admin.site.register(Evento)
admin.site.register(Feedback)
admin.site.register(Categoria)
