from pydoc import describe
from statistics import mode
from rest_framework import serializers
from .models import Assados, Avaliacoes, Produto
from decimal import Decimal

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'titulo', 'preco', 'qtd_estoque', 'categoria', 'preco_taxado']

    preco_taxado = serializers.SerializerMethodField(method_name='calcular_taxa')

    def calcular_taxa(self,produto : Produto):
        return produto.preco * Decimal(1.1)

class AssadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assados
        fields =['id','titulo','preco','qtd_estoque','categoria','preco_taxado']

    preco_taxado = serializers.SerializerMethodField(method_name='calcular_taxa')

    def calcular_taxa(self,assados : Assados):
        return assados.preco * Decimal(1.1)

# class ProdutoSerializer(serializers.Serializer):
#     id=serializers.IntegerField()
#     titulo = serializers.CharField(max_length=255)
#     preco = serializers.DecimalField(max_digits=6, decimal_places=2)

#     preco_taxado = serializers.SerializerMethodField(method_name='calcular_taxa')

#     def calcular_taxa(self,produto : Produto):
#         return produto.preco * Decimal(1.1)

class AvaliacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Avaliacoes
        # fields = '__all__'
        fields = ['id','produto','nome','descricao','dt_pedido','estrelas']