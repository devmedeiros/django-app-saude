import django_tables2 as tables
from django_tables2.utils import A
from django.utils.html import format_html
from .models import pessoa, procedimento

class pessoa_table(tables.Table):
    nome = tables.LinkColumn("pessoa_update_alias", args=[A("pk")])
    email = tables.LinkColumn("pessoa_update_alias", args=[A("pk")])
    celular = tables.LinkColumn("pessoa_update_alias", args=[A("pk")])
    funcao = tables.LinkColumn("pessoa_update_alias", args=[A("pk")])
    nascimento = tables.LinkColumn("pessoa_update_alias", args=[A("pk")])
    ativo = tables.Column()
    id = tables.LinkColumn("pessoa_delete_alias", args=[A("pk")], verbose_name="Excluir")
    
    class Meta:
        model = pessoa
        attrs = {"class": "table thead-light table-striped table-hover"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ('nome', 'email', 'celular', 'funcao', 'nascimento', 'ativo')

class procedimento_table(tables.Table):
    procedimento = tables.LinkColumn("procedimento_update_alias", args=[A("pk")])
    data_execucao = tables.LinkColumn("procedimento_update_alias", args=[A("pk")])
    paciente = tables.LinkColumn("procedimento_update_alias", args=[A("pk")])
    medico = tables.LinkColumn("procedimento_update_alias", args=[A("pk")])
    id = tables.LinkColumn("procedimento_delete_alias", args=[A("pk")], verbose_name="Excluir")
    
    class Meta:
        model = procedimento
        attrs = {"class": "table thead-light table-striped table-hover"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ('procedimento', 'data_execucao', 'paciente', 'medico')