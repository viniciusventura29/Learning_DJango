from pyexpat import model
from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=255)
    def __str__(self):
        return self.categoria


class Produto(models.Model):
    titulo = models.CharField(max_length=255)
    descritivo = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    qtd_estoque = models.PositiveSmallIntegerField()
    categoria = models.ForeignKey(Categoria,on_delete=models.PROTECT)
    

    def __str__(self):  
        return self.titulo


class Cliente(models.Model):
    titulo = models.CharField(max_length=50)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=15, primary_key=True)

    def __str__(self):  
        return self.titulo
    

class Endereco(models.Model):
    rua = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    numero = models.IntegerField()
    cpf = models.ForeignKey(Cliente,on_delete=models.PROTECT)

    def __str__(self):  
        return self.rua

class Pedido(models.Model):
    STATUS_PAGO = 'P'
    STATUS_CANCELADO = 'C'
    STATUS_AGUARDANDO = 'A'

    STATUS_PG = [
        (STATUS_AGUARDANDO, "Aguardando"),
        (STATUS_CANCELADO, "Cancelado"),
        (STATUS_PAGO, "Pago"),
    ]

    dt_pedido = models.DateTimeField(auto_now_add=True)
    status_pagamento = models.CharField(max_length=1, choices=STATUS_PG, default=STATUS_AGUARDANDO)
    cpf = models.ForeignKey(Cliente,on_delete=models.PROTECT)


class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    id_produto = models.ForeignKey(Produto, on_delete=models.PROTECT)

class Assados(models.Model):

    titulo = models.CharField(max_length=25)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    qtd_estoque = models.PositiveSmallIntegerField()
    categoria = models.ForeignKey(Categoria,on_delete=models.PROTECT)
    status_pagamento = models.ForeignKey(Pedido,on_delete=models.PROTECT)

    def __str__(self):  
        return self.titulo


class Avaliacoes(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    dt_pedido = models.DateField(auto_now_add=True)
    estrelas = models.PositiveSmallIntegerField()