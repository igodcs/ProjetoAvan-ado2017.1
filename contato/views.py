from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from contato.models import Contato
from contato.forms import ContatoForm
from contato.forms import ContactForm

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass  # não faz nada, apenas desencadeia a validação
    else:
        form = ContactForm()
    return render(request, 'contato/index.html', {'form': form})



def contact(request):
    """ A example of form """
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        
    else:
        form = ContatoForm()

    context_dict = {'form': form}
    return render(request,'contact.html', {'form': form})


class contato_(CreateView):
    template_name = 'contato/contact.html'
    model = Contato
    success_url = reverse_lazy('contato')

