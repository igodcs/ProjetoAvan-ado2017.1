from django.forms import ModelForm
from consultas.models import Consulta

class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = ["medico", "paciente", "codigo"]
