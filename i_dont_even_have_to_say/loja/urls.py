from cgitb import lookup
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = routers.DefaultRouter()
# router.register('avaliacoes',views.AvaliacoesListarViewSet)
router.register('produtos',views.ProdutosListarViewSet)

produto_router = routers.NestedDefaultRouter(router,'produtos', lookup='produtos')
produto_router.register('avaliacoes',views.AvaliacoesListarViewSet)
urlpatterns = router.urls + produto_router.urls


# urlpatterns= [
#     path('produtos/', views.ProdutosListar.as_view()),
#     path('produtos/<int:pk>/', views.ProdutosDetalhe.as_view()),
#     path('assados/', views.AssadosListar.as_view()),
#     path('assados/<int:pk>',views.AssadosDetalhes.as_view()),
#     path('avaliacoes/', views.AvaliacaoListar.as_view()),
#     path('avaliacoes/<int:pk>',views.AvaliacaoDetalhes.as_view()),
#     path('categorias/', views.CategoriaListar.as_view()),
#     path('categorias/<int:pk>',views.CategoriaDetalhes.as_view()),
#     path('avaliacoes/', views.avaliacao_listar),
 #]