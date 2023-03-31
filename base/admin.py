from django.contrib import admin
from base.models import Tabela

@admin.register(Tabela)
class ContatoAdmin(admin.ModelAdmin):
    pass

