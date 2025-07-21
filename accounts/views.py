from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User # venv > lib64 > django > contrib > auth > models.py > User(Abstract)...
from django.contrib.auth import authenticate, login

#Criando um usuário
def cadastro_view(request):
    if request.method == 'GET': #Se o usuário SOMENTE ACESSOU a página
        return render(request, 'accounts/cadastro.html')
    else: #Senão for GET, é POST, usuário enviou os dados, clicou no botão Cadastrar
        username = request.POST.get('nome') #Recebendo os dados
        senha = request.POST.get('senha') #Recebendo os dados

        user = User.objects.filter(username=username).first() #Se já tiver esse usuário no banco, armazena na variável user

        if user:
            return HttpResponse('Já existe um usuário com esse nome')
        else:
            user = User.objects.create_user(username=username, password=senha)
            return redirect('login_view')

#Entrando, logando com esse usuário
def login_view(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    else:
        username = request.POST.get('nome') #Recebendo os dados
        senha = request.POST.get('senha') #Recebendo os dados

        user = authenticate(username=username, password=senha) #TENTA autenticar com os dados fornecidos

        if user:
            login(request, user)
            return HttpResponse('Autenticado')
        else:
            return HttpResponse('E-mail ou senha inválidos')
        