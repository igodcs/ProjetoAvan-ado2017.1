from django.forms import ModelForm
from contato.models import Contato
from django import forms

class ContactForm(forms.Form):
    nome = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    mensagem = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Escreva aqui a sua mensagem!'
    )
    source = forms.CharField(       # Uma entrada escondida para uso interno
        max_length=50,              # Diga a partir de qual página o usuário enviou a mensagem
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        nome = cleaned_data.get('nome')
        email = cleaned_data.get('email')
        mensagem = cleaned_data.get('mensagem')
        if not nome and not email and not mensagem:
            raise forms.ValidationError('Você tem que escrever alguma coisa!')
    

class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'texto', 'email']


class ColorfulContactForm(forms.Form):
    nome = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'style': 'border-color: blue;',
                'placeholder': 'Escreva seu nome aqui'
            }
        )
    )
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'style': 'border-color: green;'})
    )
    mensagem = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={'style': 'border-color: orange;'}),
        help_text='Escreva aqui a sua mensagem!'
    )