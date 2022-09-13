from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreatAPIView
from .models import Avaliacoes, Produto,Assados
from .serializer import AssadosSerializer, ProdutoSerializer, AvaliacoesSerializer
from loja import serializer

# Modo com viewSet / mais abstraido
class ProdutosListarViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

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

class Assados(viewsets.ModelViewSet):
    queryset = Assados.objects.all()
    serializer_class = AssadosSerializer

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

#Modo Abstraido
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacoesSerializer

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