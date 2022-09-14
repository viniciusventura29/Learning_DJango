from django_filters.rest_framework import filterSet
from .models import Produto

class ProdutoFiltro(filterSet):
    class Meta:
        model = Produto

    
    fields = {
        'categoria_id':['exact'],
        'preco':['gt','lt'],
    }