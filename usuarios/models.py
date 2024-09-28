from django.db import models

class User(models.Model):
    name = models.CharField('Primeiro nome', max_length=255)
    username = models.CharField('Usuário', max_length=255)
    password = models.CharField('Senha', max_length=255)
    autenticado = models.BooleanField('Autenticado')

    class Meta:
        db_table = 'usuarios' 
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.username