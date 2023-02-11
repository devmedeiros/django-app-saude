from django.contrib import admin
from .models import *

class PessoaCustomizado(admin.ModelAdmin):
    list_display = ('nome', 'email', 'celular', 'funcao', 'calcula_idade', 'ativo')

    @admin.display(description='Idade')
    def calcula_idade(self, obj):
        from datetime import date
        hoje = date.today()
        idade = hoje.year - obj.nascimento.year
        return idade

class ProcedimentoCustomizado(admin.ModelAdmin):
    list_display = ('procedimento', 'data_execucao', 'paciente', 'medico')
    

admin.site.register(pessoa, PessoaCustomizado)
admin.site.register(procedimento, ProcedimentoCustomizado)