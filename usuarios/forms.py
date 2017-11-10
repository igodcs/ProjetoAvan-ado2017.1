from django import forms

class UsuarioForm(forms.Form):
	CHOICES_TIPO = (('paciente', 'Paciente'),('medico', 'Medico'),('recepcionista','Recepcionista'))
	login = forms.CharField(label='Login', max_length=30)
	senha = forms.CharField(label='Senha', max_length=30, widget=forms.PasswordInput())
	telefone = forms.CharField(label='Telefone', max_length=15)
	endereco = forms.CharField(label='Endereço', max_length=100)
	tipo = forms.ChoiceField(label='Tipo', choices=CHOICES_TIPO)

class LoginForm(forms.Form):
	login = forms.CharField(label='Login', max_length=30)
	senha = forms.CharField(label='Senha', max_length=30, widget=forms.PasswordInput())
