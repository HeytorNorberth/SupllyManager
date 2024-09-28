from django.shortcuts import render, redirect
from fornecedores.models import Fornecedor
from usuarios.models import User
from django.db import connection
from django.contrib import messages
from django.http import Http404


def index(request):
    if 'username' in request.session:
        username = request.session['username']
        
        try:
            user = User.objects.get(username=username)
            
            if user.autenticado:
                fornecedores = Fornecedor.objects.filter(user=user)
                context = {
                    'usuario':user,
                    'fornecedores':fornecedores,
                }
                return render(request, 'index.html', context)
            else:
                return redirect('login')
        except User.DoesNotExist:
            return redirect('login')
    else:
        return redirect('login')


def cadastrar_fornecedor(request):
    if 'username' in request.session:
        username = request.session['username']

        try:
            user = User.objects.get(username=username)

            if user.autenticado:
                if request.method == 'POST':
                    nome = request.POST.get('nome')
                    descricao = request.POST.get('descricao')
                    user_id = user.id

                    query = f"INSERT INTO fornecedores (nome, descricao, is_active, user_id) VALUES ('{nome}', '{descricao}', 'TRUE', '{user_id}');"
                    with connection.cursor() as cursor:
                        cursor.execute(query)
                    
                    messages.success(request, 'Fornecedor cadastrado com sucesso.')
                    return redirect('index')
                else:
                    return redirect('index')
            else:
                return redirect('login')
        except user.DoesNotExist:
            return redirect('login')

def deletar_fornecedor(request, id):
    if 'username' in request.session:
        username = request.session['username']

        try:
            user = User.objects.get(username=username)

            if user.autenticado:
                query = f"DELETE FROM fornecedores WHERE id = '{id}'"

                with connection.cursor() as cursor:
                    cursor.execute(query)
                    rows_affected = cursor.rowcount
                
                if rows_affected > 0: 
                    messages.success(request, 'Fornecedor deletado com sucesso.')
                    return redirect('index')
                else:
                    raise Http404('Fornecedor não encontrado')
            else:
                return redirect('login')
        except user.DoesNotExist:
            return redirect('login')


def ativar_fornecedor(request, id):
    if 'username' in request.session:
        username = request.session['username']

        try:
            user = User.objects.get(username=username)

            if user.autenticado:
                query = f"UPDATE fornecedores SET is_active = TRUE WHERE id = '{id}'"

                with connection.cursor() as cursor:
                    cursor.execute(query)
                    rows_affected = cursor.rowcount

                if rows_affected> 0:
                    messages.success(request, 'Fornecedor ativado com sucesso.')
                    return redirect('index')
                else:
                    raise Http404('Fornecedor não encontrado')
            else:
                return redirect('login')
        except User.DoesNotExist:
            return redirect('login')

def desativar_fornecedor(request, id):
    if 'username' in request.session:
        username = request.session['username']

        try:
            user = User.objects.get(username=username)

            if user.autenticado:
                query = f"UPDATE fornecedores SET is_active = FALSE WHERE id = '{id}'"

                with connection.cursor() as cursor:
                    cursor.execute(query)
                    rows_affected = cursor.rowcount

                if rows_affected> 0:
                    messages.success(request, 'Fornecedor desativado com sucesso.')
                    return redirect('index')
                else:
                    raise Http404('Fornecedor não encontrado')
            else:
                return redirect('login')
        except User.DoesNotExist:
            return redirect('login')