from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('avaliacoes',views.AvaliacaoViewSet, basename='avaliacoes')
router.register('produtos',views.ProdutosListarViewSet, basename='produtos')

urlpatterns= router.urls
# [
#     path('produtos/', views.produtos_listar),
#     path('produtos/<int:id>/', views.produtos_detalhes),
#     path('assados/', views.assados_listar),
#     path('assados/<int:id>',views.assados_detalhes),
#     path('avaliacoes/', views.avaliacao_listar),
# ]