from django.shortcuts import render
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django_filters.views import FilterView

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django_tables2 import SingleTableView
from django.contrib.auth.mixins import UserPassesTestMixin

def index(request):
    return HttpResponse('Pessoas')

class pessoa_create(CreateView):
    from .models import pessoa
    model = pessoa
    fields = ['nome', 'email', 'celular', 'funcao', 'nascimento', 'ativo']
    success_url = reverse_lazy('pacientes_alias')
    def test_func(self):
        return self.request.user.has_perm('pessoas.add_pessoa')

class procedimento_create(CreateView):
    from .models import procedimento
    model = procedimento
    fields = ['procedimento', 'data_execucao', 'paciente', 'medico']
    success_url = reverse_lazy('procedimentos_alias')
    def test_func(self):
        return self.request.user.has_perm('pessoas.add_pessoa')

class pessoa_update(UserPassesTestMixin, UpdateView):
    from .models import pessoa
    model = pessoa
    fields = ['nome', 'email', 'celular', 'funcao', 'nascimento', 'ativo']
    success_url = reverse_lazy('pacientes_alias')
    def test_func(self):
        return self.request.user.has_perm('pessoas.change_pessoa')

class procedimento_update(UserPassesTestMixin, UpdateView):
    from .models import procedimento
    model = procedimento
    fields = ['procedimento', 'data_execucao', 'paciente', 'medico']
    success_url = reverse_lazy('procedimentos_alias')
    def test_func(self):
        return self.request.user.has_perm('pessoas.change_procedimento')

class pessoa_delete(UserPassesTestMixin, DeleteView):
    from .models import pessoa
    model = pessoa
    fields = ['nome', 'email', 'celular', 'funcao', 'nascimento', 'ativo']
    template_name_suffix = '_delete'
    success_url = reverse_lazy('pacientes_alias')
    def test_func(self):
        return self.request.user.has_perm('pessoas.delete_pessoa')

class procedimento_delete(UserPassesTestMixin, DeleteView):
    from .models import procedimento
    model = procedimento
    fields = ['procedimento', 'data_execucao', 'paciente', 'medico']
    template_name_suffix = '_delete'
    success_url = reverse_lazy('procedimentos_alias')
    def test_func(self):
        return self.request.user.has_perm('pessoas.delete_procedimento')

@login_required(login_url='index_alias')
def home(request):
    from .models import pessoa
    dicionario = {}
    query_funcao = "select id, nome, funcao from pessoas_pessoa where nome = '%s';" % request.user.get_full_name()
    query = """
    select
        a.id
        ,procedimento
        ,data_execucao
        ,b.nome as nome_medico
        ,c.nome as nome_paciente
    from 
        pessoas_procedimento a
        left join pessoas_pessoa b on a.medico_id = b.id
        left join pessoas_pessoa c on a.paciente_id = c.id
    where 
        b.nome = '%s'
        or c.nome = '%s'
    order by data_execucao desc
    limit 1;
    """ % (request.user.get_full_name(), request.user.get_full_name())
    dicionario['funcao'] = pessoa.objects.raw(query_funcao)
    dicionario['informacoes'] = pessoa.objects.raw(query)
    return render(request, 'home.html', dicionario)

class pacientes(SingleTableView, FilterView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("pessoas.view_pessoa"):
            return super().dispatch(request, *args, **kwargs)
        else:
            return render(request, 'pacientes_restricted.html')
    from .models import pessoa
    from .tables import pessoa_table
    model = pessoa
    table_class = pessoa_table
    template_name_suffix = '_pacientes'
    table_pagination = {"per_page": 5}
    def get_queryset(self):
        from .models import pessoa
        user = self.request.user
        if user.is_staff:
            return pessoa.objects.all()
        else:
            return pessoa.objects.filter(funcao = 'PA')
    template_name = 'pessoas/pacientes.html'

class procedimentos(SingleTableView, FilterView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("pessoas.view_procedimento"):
            return super().dispatch(request, *args, **kwargs)
        else:
            return render(request, 'procedimentos_restricted.html')
    from .models import procedimento
    from .tables import procedimento_table
    model = procedimento
    table_class = procedimento_table
    template_name_suffix = '_procedimento'
    table_pagination = {"per_page": 5}
    def get_queryset(self):
        from .models import procedimento
        user = self.request.user
        if user.is_staff:
            query = """
            SELECT 
                a.id
            FROM 
                pessoas_procedimento a
                left join pessoas_pessoa b on b.id = a.paciente_id
                left join pessoas_pessoa c on c.id = a.medico_id
            """
            return procedimento.objects.raw(query)
        else:
            name = f"{user.first_name} {user.last_name}"
            query = """
            SELECT 
                a.id
            FROM 
                pessoas_procedimento a
                left join pessoas_pessoa b on b.id = a.paciente_id
                left join pessoas_pessoa c on c.id = a.medico_id
            WHERE
                b.nome = '%s'
                or c.nome = '%s'
            """ % (name, name)
            return procedimento.objects.raw(query)
    template_name = 'pessoas/procedimentos.html'

def pessoa_download(request):
    import pandas as pd
    from .models import pessoa
    eixo_y = []
    p = pessoa.objects.all()
    for _regs in p:
        eixo_x = []
        eixo_x.append(_regs.id)
        eixo_x.append(_regs.nome)
        eixo_x.append(_regs.email)
        eixo_x.append(_regs.celular)
        eixo_x.append(_regs.nascimento)
        eixo_x.append(_regs.funcao)
        eixo_x.append(_regs.ativo)
        eixo_y.append(eixo_x)
    _rotulos_colunas = []
    _rotulos_colunas.append("id")
    _rotulos_colunas.append("nome")
    _rotulos_colunas.append("email")
    _rotulos_colunas.append("celular")
    _rotulos_colunas.append("nascimento")
    _rotulos_colunas.append("funcao")
    _rotulos_colunas.append("ativo")
    df = pd.DataFrame(eixo_y, columns=_rotulos_colunas)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=pessoas.csv'
    df.to_csv(path_or_buf=response, index=False)
    return response

def procedimento_download(request):
    import pandas as pd
    from .models import procedimento
    eixo_y = []
    p = procedimento.objects.all()
    for _regs in p:
        eixo_x = []
        eixo_x.append(_regs.id)
        eixo_x.append(_regs.procedimento)
        eixo_x.append(_regs.data_execucao)
        eixo_x.append(_regs.paciente)
        eixo_x.append(_regs.medico)
        eixo_y.append(eixo_x)
    _rotulos_colunas = []
    _rotulos_colunas.append("id")
    _rotulos_colunas.append("procedimento")
    _rotulos_colunas.append("data_execucao")
    _rotulos_colunas.append("paciente")
    _rotulos_colunas.append("medico")
    df = pd.DataFrame(eixo_y, columns=_rotulos_colunas)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=procedimentos.csv'
    df.to_csv(path_or_buf=response, index=False)
    return response

### Login
def index(request):
    usuario = request.POST.get('username')
    senha = request.POST.get('password')
    user = authenticate(username=usuario, password=senha)
    if (user is not None):
        login(request, user)
        request.session['username'] = usuario
        request.session['password'] = senha
        request.session['usernamefull'] = user.get_full_name()
        from django.shortcuts import redirect
        return redirect('home_alias')
    else:
        return render(request, 'index.html')
