from django.contrib import admin
from fornecedores.models import Fornecedor

@admin.register(Fornecedor)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'is_active')