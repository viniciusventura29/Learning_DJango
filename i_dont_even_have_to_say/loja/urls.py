from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('avaliacoes',views.Avaliacao.as_view(), basename='avaliacoes')
# router.register('produtos',views.ProdutosListar.as_view(), basename='produtos')

urlpatterns= [
    path('produtos/', views.ProdutosListar.as_view()),
    path('produtos/<int:pk>/', views.ProdutosDetalhe.as_view()),
    path('assados/', views.AssadosListar.as_view()),
    path('assados/<int:pk>',views.AssadosDetalhes.as_view()),
    path('avaliacoes/', views.AvaliacaoListar.as_view()),
    path('avaliacoes/<int:pk>',views.AvaliacaoDetalhes.as_view()),
    path('categorias/', views.CategoriaListar.as_view()),
    path('categorias/<int:pk>',views.CategoriaDetalhes.as_view()),
#     path('avaliacoes/', views.avaliacao_listar),
 ]