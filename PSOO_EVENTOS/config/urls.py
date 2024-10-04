from django.contrib import admin
from django.urls import path
from app.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    path("pessoa/", PessoaView.as_view(template_name = 'pessoa.html'), name="pessoa"),
    path("atividade/", AtividadeView.as_view(template_name = 'atividade.html'), name="atividade"),
    path("inscricao/", InscricaoView.as_view(template_name = 'inscricao.html'), name="inscricao"),
    path("local/", LocalView.as_view(template_name = 'local.html'), name="local"),
    path("ocupacao/", OcupacaoView.as_view(template_name = 'ocupacao.html'), name="ocupacao"),
    path("evento/", EventoView.as_view(template_name = 'evento.html'), name="evento"),
    path("categoria/", CategoriaView.as_view(template_name = 'categoria.html'), name="categoria"),


]


