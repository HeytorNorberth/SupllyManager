from django.db import models
from usuarios.models import User


class Fornecedor(models.Model):
    nome = models.CharField("Nome", max_length=255)
    descricao = models.TextField("Descrição")
    is_active = models.BooleanField("Ativo")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'fornecedores'
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
    
    def __str__(self):
        return self.nome