from django.urls import path
from . import views

urlpatterns=[
    path('',views.home_index, name='homeindex'),
    path('cadastrar/',views.cadastrar_music,name='cadastrar_music'),
    path('detalhes/',views.detalhes,name='detalhes'),
]