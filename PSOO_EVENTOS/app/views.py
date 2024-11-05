from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

class IndexView(View):
    def get(self, request):
        eventos = Evento.objects.all()  # Recupera todos os eventos cadastrados
        return render(request, 'index.html', {'eventos': eventos})  # Passa os eventos para o template

class AtividadeView(View):
    template_name = 'atividade.html'
    
    def get(self, request):
        atividades = Atividade.objects.all()  
        return render(request, self.template_name, {'atividades': atividades})

class LocalView(View):
    template_name = 'local.html'
    
    def get(self, request):
        locais = Local.objects.all() 
        return render(request, self.template_name, {'locais': locais})

class EventoView(View):
    template_name = 'evento.html'
    
    def get(self, request):
        eventos = Evento.objects.all()  
        return render(request, self.template_name, {'eventos': eventos})

class EventoDetalhesView(View):
    def get(self, request, id):
        evento = get_object_or_404(Evento, id=id)  # Obtém o evento pelo ID
        comentarios = Feedback.objects.filter(evento=evento)  # Obtém os comentários relacionados ao evento
        return render(request, 'evento_detalhes.html', {'evento': evento, 'comentarios': comentarios})

    def post(self, request, id):
        evento = get_object_or_404(Evento, id=id)  # Obtém o evento pelo ID
        if request.method == 'POST':
            # Obtém os dados do formulário
            avaliacao = request.POST.get('avaliacao')

            # Cria um novo comentário
            Feedback.objects.create(
                evento=evento,
                avaliacao=avaliacao,

            )
            return redirect('evento_detalhes', id=id)  # Redireciona para a página de detalhes do evento após adicionar o comentário


class CategoriaView(View):
    template_name = 'categoria.html'
    
    def get(self, request):
        categorias = Categoria.objects.all()  
        return render(request, self.template_name, {'categorias': categorias})

class FeedbackView(View):
    template_name = 'feedback.html'
    
    def get(self, request):
        feedback = Feedback.objects.all()  
        return render(request, self.template_name, {'feedback': feedback})


 