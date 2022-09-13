from pyexpat.errors import messages
from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Avaliacoes, Produto, Assados, Categoria
from .serializer import AssadosSerializer, ProdutoSerializer, AvaliacoesSerializer, CategoriaSerializer
from loja import serializer

# Modo com viewSet / mais abstraido
# class ProdutosListarViewSet(viewsets.ModelViewSet):
#     queryset = Produto.objects.all()
#     serializer_class = ProdutoSerializer

#Modo com ListCreateAPIView
class ProdutosListar(ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

#Modo com ListCreateAPIView
class ProdutosDetalhe(RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    # lookup_field = 'id'

    def update(self, request, pk):
        if float(request.data['preco']) < 0 or float(request.data['preco']) >=100:
            return Response({"error": "O preço deve ser no range de 0 a 100"})

        return super().update(request)  

    def delete(self, request, pk):
        produto = get_object_or_404(Produto, pk=pk)
        if produto.qtd_estoque != 0: 
            return Response({"error": "Só é possivel deletar produtos com o estoque zerado"})

        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request, pk):
        if float(request.data['preco']) < 0 or float(request.data['preco']) >=100:
            return Response({"error": "O preço deve ser no range de 0 a 100"})

        return super().create(request)  

# Forma manual
# @api_view(['GET', 'POST'])
# def produtos_listar(request):
    # if request.method == 'GET':
    #     produto = Produto.objects.all()
    #     serializer = ProdutoSerializer(produto, many=True)
    #     return Response(serializer.data)
    # elif request.method == "POST":
    #     serializer = ProdutoSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status = status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT',"DELETE"])
# def produtos_detalhes(request,id):
#     # try:
#     produto = get_object_or_404(Produto, pk=id)
#     if request.method == 'GET':
#         serializer = ProdutoSerializer(produto)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ProdutoSerializer(produto, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     elif request.method == 'DELETE':
#         produto.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     # except:
#         # return Response(status.HTTP_404_NOT_FOUND)


# Modo com viewSet / mais abstraido
# class Assados(viewsets.ModelViewSet):
#     queryset = Assados.objects.all()
#     serializer_class = AssadosSerializer


#Modo com ListCreateAPIView
class AssadosListar(ListCreateAPIView):
    queryset = Assados.objects.all()
    serializer_class = AssadosSerializer

class AssadosDetalhes(RetrieveUpdateDestroyAPIView):
    queryset = Assados.objects.all()
    serializer_class = AssadosSerializer

    def update(self, request, pk):
        if float(request.data['preco']) < 0 or float(request.data['preco']) >=100:
            return Response({"error": "O preço deve ser no range de 0 a 100"})

        return super().update(request)  

    def delete(self, request, pk):
        assado = get_object_or_404(Assados, pk=pk)
        if assado.qtd_estoque != 0: 
            return Response({"error": "Só é possivel deletar produtos com o estoque zerado"})

        assado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request, pk):
        if float(request.data['preco']) < 0 or float(request.data['preco']) >=100:
            return Response({"error": "O preço deve ser no range de 0 a 100"})

        return super().create(request)  

# @api_view(['GET', 'POST'])
# def assados_listar(request):
#     if request.method == 'GET':
#         assados = Assados.objects.all()
#         serializer = AssadosSerializer(assados, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = AssadosSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# @api_view()
# def assados_detalhes(request,id):
    # assado = get_object_or_404(Assados, pk=id)
    # serializer = ProdutoSerializer(assado)
    # return Response(serializer.data)



# Modo com viewSet / mais abstraido
# class AvaliacaoViewSet(viewsets.ModelViewSet):
#     queryset = Avaliacoes.objects.all()
#     serializer_class = AvaliacoesSerializer


class AvaliacaoListar(ListCreateAPIView):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacoesSerializer

class AvaliacaoDetalhes(ListCreateAPIView):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacoesSerializer

    def update(self, request, pk):
        if float(request.data['preco']) < 0 or float(request.data['preco']) >=100:
            return Response({"error": "O preço deve ser no range de 0 a 100"})

        return super().update(request)  

    def delete(self, request, pk):
        avaliacoes = get_object_or_404(Avaliacoes, pk=pk)
        if avaliacoes.qtd_estoque != 0: 
            return Response({"error": "Só é possivel deletar produtos com o estoque zerado"})

        avaliacoes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request, pk):
        if float(request.data['preco']) < 0 or float(request.data['preco']) >=100:
            return Response({"error": "O preço deve ser no range de 0 a 100"})

        return super().create(request)  


class CategoriaListar(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetalhes(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    def update(self, request, pk):
        if float(request.data['preco']) < 0 or float(request.data['preco']) >=100:
            return Response({"error": "O preço deve ser no range de 0 a 100"})

        return super().update(request)  

    def delete(self, request, pk):
        categoria = get_object_or_404(Categoria, pk=pk)
        if categoria.qtd_estoque != 0: 
            return Response({"error": "Só é possivel deletar produtos com o estoque zerado"})

        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request, pk):
        if float(request.data['preco']) < 0 or float(request.data['preco']) >=100:
            return Response({"error": "O preço deve ser no range de 0 a 100"})

        return super().create(request)  


# Modo Sem abstração (Que ja tinha abstração kk)
# @api_view(['GET','POST'])
# def avaliacao_listar(request):
#     if request.method=='GET':
#         querySet = Avaliacoes.objects.all()
#         serializer = AvaliacoesSerializer(querySet, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     elif request.method =="POST":
#         serializer = AvaliacoesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)

#         else:
#             return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)