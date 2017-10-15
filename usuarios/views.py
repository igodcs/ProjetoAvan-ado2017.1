from django.shortcuts import render
from usuarios.models import Usuario
from usuarios.forms import UsuarioForm
from django.http import HttpResponseRedirect

def index(request):
	usuarios = Usuario.objects.all()
	context_dict = {'usuarios': usuarios}
	return render(request, 'usuarios/index.html', context=context_dict)

def detalhes(request, usuario_id):
	u = Usuario.objects.get(pk=usuario_id)
	context_dict = {'usuarios': u}
	return render(request, 'usuarios/detalhes.html', context=context_dict)

def new(request):
	if request.method == 'POST':
		form = UsuarioForm(request.POST)
		form.save()
		return HttpResponseRedirect('/home/')
	else:
		form = UsuarioForm()
		context_dict = {'form': form}
		return render(request, 'usuarios/new.html', context=context_dict)

def edit(request, usuario_id):
	usuario = Usuario.objects.get(pk=usuario_id)
	if request.method == 'POST':
		form = UsuarioForm(request.POST, instance=usuario)
		form.save()
		return HttpResponseRedirect('/home/')
	else:
		form = UsuarioForm(instance=usuario)
		context_dict = {'form': form, 'usuario_id': usuario_id}
		return render(request, 'usuarios/edit.html', context=context_dict)

def delete(request, usuario_id):
	usuario = Usuario.objects.get(pk=usuario_id)
	usuario.delete()
	return HttpResponseRedirect('/usuarios/')
