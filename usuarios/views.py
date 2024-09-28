from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from usuarios.models import User

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('senha')

        query = f"SELECT * FROM usuarios WHERE username = '{username}' AND password = '{password}'"

        with connection.cursor() as cursor:
            cursor.execute(query)
            user = cursor.fetchone() 
        
        if user:
            update_query = f"UPDATE usuarios SET autenticado = TRUE WHERE username = '{username}'"
            with connection.cursor() as cursor:
                cursor.execute(update_query)
            
            request.session['username'] = username

            return redirect('index')
        else:
            messages.error(request, 'Credênciais inválidas.')
            return redirect('login')

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    
    if request.method == 'POST':
        name = request.POST.get('nome')
        username = request.POST.get('usuario')
        password = request.POST.get('senha')

        query_check = f"SELECT COUNT(*) FROM usuarios WHERE username = '{username}'"
        with connection.cursor() as cursor:
            cursor.execute(query_check)
            user_exists = cursor.fetchone()[0]
        
        if user_exists:
            messages.error(request, 'Usuário já cadastrado no sistema.')
            return redirect('cadastro')
        
        nome_usuario = username.split("'")[0]
        query_insert = f"INSERT INTO usuarios (name, username, password, autenticado) VALUES ('{name}', '{nome_usuario}', '{password}', 'False')"
        with connection.cursor() as cursor:
            cursor.execute(query_insert)

        messages.success(request, 'Usuário cadastrado com sucesso')
        return redirect('login')


def logout(request):
    if 'username' in request.session:
        username = request.session['username']

        try:
            user = User.objects.get(username=username)

            if user.autenticado:
                query = f"UPDATE usuarios SET autenticado = FALSE WHERE username = '{username}'"

                with connection.cursor() as cursor:
                    cursor.execute(query)
                
                return redirect('login')
            else:
                return redirect('login')
        except User.DoesNotExist:
            return redirect('login')