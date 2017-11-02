from django.shortcuts import render
from usuarios.forms import UsuarioForm
from django.contrib.auth.models import User
from usuarios.models import UserProfile
from usuarios.forms import LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def new(request):
	form = UsuarioForm(request.POST)

	if (form.is_valid()):
		login = form.cleaned_data['login']
		senha = form.cleaned_data['senha']
		telefone = form.cleaned_data['telefone']
		endereco = form.cleaned_data['endereco']
		tipo = form.cleaned_data['tipo']

		new_user = User.objects.create_user(login, password=senha)
		new_user.save()

		new_profile = UserProfile(user=new_user, telefone=telefone, endereco=endereco, tipo=tipo)
		new_profile.save()

		return HttpResponseRedirect('/home/')
	else:
		form = UsuarioForm()

	context_dict = {'form': form}
	return render(request, 'usuario/new.html', context=context_dict)

def user_login(request):

	form = LoginForm()

	if (request.method == "POST"):
		form = LoginForm(request.POST)

		if (form.is_valid()):
			form_login = form.cleaned_data['login']
			form_senha = form.cleaned_data['senha']

			user = authenticate(request, username=form_login, password=form_senha)

			if (user is not None):

				login(request,user)
				login_usuario = UserProfile.objects.get(user=user)
				if login_usuario.tipo == 'paciente':
					return HttpResponseRedirect('/usuarios/usuario/arearestritapaciente.html')
				elif login_usuario.tipo == 'medico':
					return HttpResponseRedirect('/usuarios/usuario/arearestritamedico.html')
				else:
					return HttpResponseRedirect('usuario/login.html')
		else:
			form = LoginForm()

	context_dict = {'form': form}
	return render(request, 'usuario/login.html', context=context_dict)

@login_required
def restricted_area_paciente(request):
	return render(request, 'usuario/arearestritapaciente.html')

def restricted_area_medico(request):
	return render(request, 'usuario/arearestritamedico.html')
