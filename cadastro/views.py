from django.shortcuts import render
from cadastro.models import Usuario

def index(request):
    return render(request, 'cadastro/index.html')

def cadastro(request):
	usuarios = Usuario.objects.all()
	context_dict = {'usuarios': usuarios}
	return render(request, 'cadastro/usuarios.html', context=context_dict)

def detail(request, produto_id):
	u = Usuario.objects.get(userk=produto_id)
	context_dict = {'produtos': u}
	return render(request, 'cadastro/detail.html', context=context_dict)
