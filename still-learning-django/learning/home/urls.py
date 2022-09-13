from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_index, name='homeindex'),
    path('cadastrar_prod/', views.cadastrar_prod, name='cadastrar_prod'),
    path('details/<str:name>',views.details, name='details')
]