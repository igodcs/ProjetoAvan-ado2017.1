from django.shortcuts import render
from usuarios.models import Usuario

def index(request):
	usuarios = Usuario.objects.all()
	context_dict = {'usuarios': usuarios}
	return render(request, 'usuarios/index.html', context=context_dict)

def detalhes(request, usuario_id):
	u = Usuario.objects.get(pk=usuario_id)
	context_dict = {'usuarios': u}
	return render(request, 'usuarios/detalhes.html', context=context_dict)
