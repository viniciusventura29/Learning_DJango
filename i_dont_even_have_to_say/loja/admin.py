from django.contrib import admin
from . import models

admin.site.register(models.Produto)
admin.site.register(models.Categoria)
admin.site.register(models.Assados)
admin.site.register(models.Pedido)
admin.site.register(models.Endereco)
admin.site.register(models.Cliente)
admin.site.register(models.Avaliacoes)
