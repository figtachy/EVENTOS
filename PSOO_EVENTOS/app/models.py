from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    senha = models.CharField(max_length=15)
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()
    email = models.TextField()
    class Meta:
        verbose_name_plural = "Pessoas"
    def __str__(self):
        return self.nome
    
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
    
class Inscricao(models.Model):
    estado = models.CharField(max_length=20)
    evento = models.ForeignKey('Evento', on_delete=models.CASCADE)
    participante = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Inscrições"
    def __str__(self):
        return f'{self.participante} - {self.estado}'
    
class Local(models.Model):
    nome = models.CharField(max_length=50)
    referencia = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Locais"
    def __str__(self):
        return self.nome
    
class Ocupacao(models.Model):
    nome = models.CharField(max_length=50)
    setor = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Ocupações"
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
    class Meta:
        verbose_name_plural = "Eventos"
    def __str__(self):
        return self.descricao
    
class Feedback(models.Model):
    avaliacao = models.CharField(max_length=20)
    palestrante = models.CharField(max_length=50)
    duracao = models.TimeField()
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

