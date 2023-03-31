from django import forms
from base.models import Tabela

class TabelaForm(forms.ModelForm):
    class Meta:
        model = Tabela
        fields = ['nome','cep','endereco','bairro','cidade','uf','telefone']