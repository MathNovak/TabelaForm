from django.shortcuts import render
from base.forms import TabelaForm

def inicio(request):
    return render(request, 'index.html')

def tabela(request):
    sucesso = False
    form = TabelaForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    contexto = {
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'tabela.html', contexto)
