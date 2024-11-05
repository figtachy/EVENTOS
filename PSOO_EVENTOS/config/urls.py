from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    path("atividade/", AtividadeView.as_view(template_name='atividade.html'), name="atividade"),
    path("local/", LocalView.as_view(template_name='local.html'), name="local"),
    path("evento/", EventoView.as_view(template_name='evento.html'), name="evento"),
    path("categoria/", CategoriaView.as_view(template_name='categoria.html'), name="categoria"),
    path("feedback/", FeedbackView.as_view(template_name='feedback.html'), name="feedback"),
    path('evento/<int:id>/', EventoDetalhesView.as_view(), name='evento_detalhes'),  # Nova URL para detalhes do evento
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
