from django.shortcuts import render, redirect
from myapp.forms import UsersForm
from myapp.models import usuario

# Create your views here.

def home(request):
    tabela = usuario.objects.all()
    return render(request, 'home.html',{'usuario':tabela})

def cafe(request):
    return render(request, 'cafe.html')

def novo_arquivo(request):
    return render(request, 'novo_arquivo.html')

def cadastro(request):
    data = {}
    data['form'] = UsersForm()
    return render(request,'cadastro.html',data)

def docad(request):
    users = usuario.objects.all()
    form = UsersForm(request.POST or None)
    erro = ''
    for c in users:
        if form['usuario'].data == c.usuario:
            erro = 'User already exists'
    if form.is_valid() and erro == '':
        form.save()
    return redirect('home')