from django.contrib import admin
from usuarios.models import User

@admin.register(User)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'autenticado')