from django.shortcuts import render
from consultas.models import Consulta
from consultas.forms import ConsultaForm
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
		return HttpResponseRedirect('/home/')
	else:
		form = ConsultaForm()

	context_dict = {'form': form}
	return render(request, 'consultas/new.html', context=context_dict)

def edit(request, consulta_id):
	consulta = Consulta.objects.get(pk=consulta_id)
	if request.method == 'POST':
		form = ConsultaForm(request.POST, instance=consulta)
		form.save()
		return HttpResponseRedirect('/home/')
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
