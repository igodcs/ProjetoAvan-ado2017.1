from django.shortcuts import render
from consultas.models import Consulta
from consultas.forms import ConsultaForm
from usuarios.models import UserProfile
from usuarios.forms import UsuarioForm
from usuarios.forms import LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def index(request):
	consultas = Consulta.objects.all()
	context_dict = {'consultas': consultas}
	return render(request, 'consultas/index.html', context=context_dict)

def detalhes(request, consulta_id):
	c = Consulta.objects.get(pk=consulta_id)
	context_dict = {'consulta': c}
	return render(request, 'consultas/detalhes.html', context=context_dict)

def new(request):
	if request.method == 'POST':
		form = ConsultaForm(request.POST)
		form.save()

	else:
		form = ConsultaForm()

	context_dict = {'form': form}
	return render(request, 'consultas/new.html', context=context_dict)

def edit(request, consulta_id):
	consulta = Consulta.objects.get(pk=consulta_id)
	if request.method == 'POST':
		form = ConsultaForm(request.POST, instance=consulta)
		form.save()
		return HttpResponseRedirect('/consultas/')
	else:
		form = ConsultaForm(instance=consulta)

	context_dict = {'form': form, 'consulta_id': consulta_id}
	return render(request, 'consultas/edit.html', context=context_dict)

def delete(request, consulta_id):
	consulta = Consulta.objects.get(pk=consulta_id)
	consulta.delete()
	return HttpResponseRedirect('/consultas/')

def consultarestrita(request):
	consultas = Consulta.objects.all()
	context_dict = {'consultas': consultas}
	return render(request, 'consultas/consultarestrita.html', context=context_dict)

def consultarestritamedico(request):
	user = request.user
	login(request,user)
	login_usuario = UserProfile.objects.get(user=user)
	if login_usuario.tipo == 'medico':
		consultas = Consulta.objects.filter(medico=login_usuario.user.username)
		context_dict = {'consultas': consultas}
		return render(request, 'consultas/consultarestritamedico.html', context=context_dict)
#------------------------------------------------------------------------------------------------
	#user = request.user
	#consultas = Consulta.objects.filter(medico=user.login)
	#context_dict = {'consultas': consultas}
	#return render(request, 'consultas/consultarestritamedico.html', context=context_dict)
#------------------------------------------------------------------------------------------------

def consultarestritapaciente(request):
	user = request.user
	login(request,user)
	login_usuario = UserProfile.objects.get(user=user)
	if login_usuario.tipo == 'paciente':
		consultas = Consulta.objects.filter(paciente=login_usuario.user.username)
		context_dict = {'consultas': consultas}
		return render(request, 'consultas/consultarestritapaciente.html', context=context_dict)
