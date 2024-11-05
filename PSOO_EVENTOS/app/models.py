from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Atividade(models.Model):
    descricao = models.CharField(max_length=100)
    data_inicio = models.DateField()
    hora_inicio = models.TimeField()
    data_fim = models.DateField()
    hora_fim = models.TimeField()
    evento = models.ForeignKey('Evento', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Atividades"

    def __str__(self):
        return self.descricao


class Local(models.Model):
    nome = models.CharField(max_length=50)
    referencia = models.CharField(max_length=50)
    link_maps = models.URLField(max_length=255, blank=True, null=True)  # Campo para o link do Google Maps


    class Meta:
        verbose_name_plural = "Locais"

    def __str__(self):
        return self.nome

class Evento(models.Model):
    descricao = models.TextField()
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    hora_inicio = models.TimeField()
    data_fim = models.DateField()
    hora_fim = models.TimeField()
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='eventos/', blank=True, null=True)  # Novo campo para a imagem


    class Meta:
        verbose_name_plural = "Eventos"

    def __str__(self):
        return self.descricao


class Feedback(models.Model):
    avaliacao = models.CharField(max_length=20)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Feedbacks"

    def __str__(self):
        return self.avaliacao


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome
