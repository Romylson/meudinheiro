from django.db import models
from django.contrib.auth.models import User
from geral.models import Categoria
# Create your models here.



class Movimentacao(models.Model):
    descricao = models.CharField(verbose_name='Descrição', max_length=70)
    discriminacao = models.TextField(verbose_name='Discriminação', blank=True, null=True)
    valor = models.DecimalField(verbose_name='Valor R$', max_digits=19, decimal_places=2)
    categoria = models.ForeignKey(Categoria, verbose_name='Categoria', on_delete=models.PROTECT)
    anexo = models.FileField(verbose_name='Upload Anexo', upload_to='anexos', blank=True, null=True)
    usuario = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE, null=True)
    data_criacao = models.DateTimeField(verbose_name='Data Criação', auto_now_add=True)
    data_alteracao = models.DateTimeField(verbose_name='Data Alteração', auto_now=True)


    class Meta:
        verbose_name = 'Movimentação'
        verbose_name_plural = 'Movimentações'

    def __str__(self):
        return self.descricao
