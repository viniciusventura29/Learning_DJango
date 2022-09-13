# Generated by Django 4.0.6 on 2022-09-01 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('titulo', models.CharField(max_length=50)),
                ('idade', models.IntegerField()),
                ('cpf', models.CharField(max_length=15, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_pedido', models.DateTimeField(auto_now_add=True)),
                ('status_pagamento', models.CharField(choices=[('A', 'Aguardando'), ('C', 'Cancelado'), ('P', 'Pago')], default='A', max_length=1)),
                ('cpf', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='loja.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descritivo', models.TextField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6)),
                ('qtd_estoque', models.PositiveSmallIntegerField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='loja.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.produto')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='loja.pedido')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
                ('cpf', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='loja.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Assados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=25)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6)),
                ('qtd_estoque', models.PositiveSmallIntegerField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='loja.categoria')),
                ('status_pagamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='loja.pedido')),
            ],
        ),
    ]