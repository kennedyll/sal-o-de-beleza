from calendar import c
from plistlib import UID
from django.shortcuts import render, redirect, HttpResponse
from myapp.forms import UsersForm, LoginForm, ComentariosForm
from myapp.models import Usuario, Comentario

# Create your views here.

def home(request):
    tabela = Usuario.objects.all()
    return render(request, 'home.html',{'usuario':tabela})

def cafe(request):
    return render(request, 'cafe.html')

def salao_home(request):
    return render(request, 'salao_home.html')

def novo_arquivo(request):
    return render(request, 'novo_arquivo.html')

def cadastro(request):
    data = {}
    data['form'] = UsersForm()
    return render(request,'cadastro.html',data)

def login(request):
    data = {}
    data['login'] = LoginForm()
    return render(request, 'login.html', data)

def docad(request):
    tabela = Usuario.objects.all()
    form = UsersForm(request.POST or None)
    print(form)
    erro = ''
    for c in tabela:
        if form['usuario'].data == c.usuario:
            erro = 'User already exists'
    if form.is_valid() and erro == '':
        form.save()
        return redirect('home')

def perfil(request):
    profile = {}
    try:
        profile ['perfil'] = UsersForm(instance=Usuario.objects(id=request.session['uid']))
        return render(request, 'profile.html', profile)
    except:
        return HttpResponse("voce nao esta logado")

def doupdate(request):
    form = Usuario.objects.get(id=request.session['uid'])
    form.usuario = request.POST['usuario']
    form.senha = request.POST['senha']
    form.nome = request.POST['nome']
    form.ultimo_nome = request.POST['ultimo_nome']

    form.save()
    return redirect('home') 

def dolog(request):
    if request.method == 'POST':
        try:
            user = Usuario.objects.get(usuario=request.POST['usuario']) # select * from usuario where usuario
        except:
            return HttpResponse("Falha no Login")
        print(user)
        if user.senha == request.POST['senha']:
            request.session['uid'] = user.id
            return redirect('salao')
        else:
            return HttpResponse("Falha no Login")
    else:
        redirect('cadastro')

def comentario(request):
    data = {}
    if request.method == 'POST':
        c = Comentario(usuario=Usuario.objects.get(id=request.session['uid']),comentario=request.POST['comentario'])
        c.save()
        return redirect('comentario')
    else:
        data['forms'] = ComentariosForm()
        data['history'] = Comentario.objects.filter(usuario=request.session['uid'])
    return render(request, 'comentario.html', data)

def edit_coment(request, id):
    c = Comentario.objects.get(id=id)
    if request.method == 'POST':
        f = ComentariosForm(request.POST, instance=c)
        f.save()
        return redirect('comentario')

    else:
        f = ComentariosForm(instance=c)
        return render(request, 'comentario.html', {'forms':f})
