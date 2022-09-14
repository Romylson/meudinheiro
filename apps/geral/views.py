from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoriaForm, LoginForm,UserForm
from django.contrib import messages
from .models import Categoria
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def principal(request):
    template_name = 'base.html'
    return render(request, template_name, {})

def login_usuario(request):
    template_name = 'geral/login_usuario.html'
    context = {}
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            senha = form.cleaned_data.get('password')
            usr = authenticate(username=usuario, password=senha)
            if usr:
                login(request,usr)
                return redirect('geral:principal')
            else:
                messages.error(request, 'Usuário ou senha inválidos')
                return redirect('geral:login_usuario')
    else:
        form = LoginForm()
    context['form'] = form
    return render(request, template_name, context)
@login_required
def logout_usuario(request):
    logout(request)
    return redirect('geral:login_usuario')

def novo_usuario(request):
    template_name = 'geral/novo_usuario.html'
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.set_password(f.password)
            f.save()
            messages.success(request, 'Usuário criado com sucesso')
            return redirect('geral:login_usuario')
        else:
            messages.error(request, 'Corrija os erros do seu formulário')
            form = UserForm(request.POST)
            context['form'] = form
            return render(request, template_name, context)
    else:
        form = UserForm()
    context['form'] = form
    return render(request, template_name, context)
@login_required
def nova_categoria(request):
    template_name = 'geral/nova_categoria.html'
    context = {}
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.usuario = request.user
            f.save()
            messages.sucess(request, 'Categoria adicionada com sucesso.')
            return redirect('geral:lista_categorias')
        else:
            form = CategoriaForm(request.POST)
            context['form'] = form
    else:
        form = CategoriaForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required
def lista_categorias(request):
    template_name = 'geral/lista_categorias.html'
    #categorias = Categoria.objects.all() # SQL :select * from geral_categoria; <-- tudo, independente do dono
    #SQL: select * from geral_categoria where usuario='admin';
    categorias = Categoria.objects.filter(usuario=request.user) # <----somente do usuário admin
    context = {
        'categorias': categorias,
    }
    return render(request, template_name, context)

def editar_categoria(request, pk):
    template_name = 'categorias/nova_categoria.html'
    context = {}
    categoria = get_object_or_404(Categoria, pk=pk)  # Categoria.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(data=request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request,'Categoria alterada com sucesso.')
            return redirect('categorias:lista_categorias')
        else:
            form = CategoriaForm(instance=categoria)
            context['form'] = form
    else:
        form = CategoriaForm(instance=categoria)
    context['form'] = form
    return render(request, template_name, context)
def apagar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)  # Categoria.objects.get(pk=pk)
    categoria.delete()
    return redirect('categorias:lista_categorias')