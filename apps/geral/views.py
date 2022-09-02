from django.shortcuts import render, redirect
from .forms import CategoriaForm
from django.contrib import messages
from .models import Categoria
# Create your views here.


def principal(request):
    template_name = 'base.html'
    return render(request, template_name, {})

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

def lista_categorias(request):
    template_name = 'geral/lista_categorias.html'
    #categorias = Categoria.objects.all() # SQL :select * from geral_categoria; <-- tudo, independente do dono
    #SQL: select * from geral_categoria where usuario='admin';
    categorias = Categoria.objects.filter(usuario=request.user) # <----somente do usuário admin
    context = {
        'categorias': categorias,
    }
    return render(request, template_name, context)
