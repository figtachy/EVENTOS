from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

class IndexView(LoginRequiredMixin,View):
    login_url = '/pessoa/' 
    def get(self, request):
        return render(request, 'index.html',)
    def post(self, request):
        pass

class PessoaView(View):
    template_name = 'pessoa.html'
    def get(self, request):
        pessoas = Pessoa.objects.all()  
        return render(request, 'pessoa.html', {'pessoas': pessoas})
    
    def post(self, request):
        pass

class AtividadeView(View):
    template_name = 'atividade.html'
    def get(self, request):
        atividades = Atividade.objects.all()  
        return render(request, 'atividade.html', {'atividades': atividades})
    
    def post(self, request):
        pass

class InscricaoView(View):
    template_name = 'inscricao.html'
    def get(self, request):
        inscricoes = Inscricao.objects.all()  
        return render(request, 'inscricao.html', {'inscricoes': inscricoes})
    
    def post(self, request):
        pass

class LocalView(View):
    template_name = 'local.html'
    def get(self, request):
        locais = Local.objects.all() 
        return render(request, 'local.html', {'locais': locais})
    
    def post(self, request):
        pass

class OcupacaoView(View):
    template_name = 'ocupacao.html'
    def get(self, request):
        ocupacoes = Ocupacao.objects.all()  
        return render(request, 'ocupacao.html', {'ocupacoes': ocupacoes})
    
    def post(self, request):
        pass

class EventoView(View):
    template_name = 'evento.html'
    def get(self, request):
        eventos = Evento.objects.all()  
        return render(request, 'evento.html', {'eventos': eventos})
    
    def post(self, request):
        pass

class CategoriaView(View):
    template_name = 'categoria.html'
    def get(self, request):
        categorias = Categoria.objects.all()  
        return render(request, 'categoria.html', {'categorias': categorias})
    
    def post(self, request):
        pass



class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        # Renderiza o formulário de login
        return render(request, self.template_name)

    def post(self, request):
        # Recebe os dados de login
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Tenta autenticar o usuário
        user = authenticate(request, email=email, password=senha)

        if user is not None:
            # Se o usuário for autenticado com sucesso, faz o login
            login(request, user)
            return redirect('home')  # Redireciona para a página inicial após o login
        else:
            # Se falhar, mostra uma mensagem de erro
            messages.error(request, 'E-mail ou senha inválidos.')
            return render(request, self.template_name)

# Cadastro View
class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        if password != password2:
            messages.error(request, "As senhas não coincidem.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Nome de usuário já existe.")
            return redirect('register')

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        messages.success(request, "Cadastro realizado com sucesso!")
        return redirect('login')

# Logout View
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')