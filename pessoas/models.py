from django.db import models

class pessoa(models.Model):
    PACIENTE = 'PA'
    MEDICO = 'ME'
    FUNCIONARIO = 'FU'
    FUNCAO_ESCOLHA = [
        (PACIENTE, 'Paciente'),
        (MEDICO, 'Médico'),
        (FUNCIONARIO, 'Funcionário')
    ]
    nome = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nome')
    email = models.CharField(max_length=50, null=False, blank=False, verbose_name='E-mail')
    celular = models.CharField(max_length=20, null=True, blank=True, verbose_name='Celular')
    funcao = models.CharField(max_length=2, choices=FUNCAO_ESCOLHA, default=PACIENTE, verbose_name='Função')
    nascimento = models.DateField(null=True, blank=True, default='1900-01-01', verbose_name='Data de Nascimento')
    ativo = models.BooleanField(default=True, verbose_name='Cadastro Ativo')

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome', 'funcao',]

class procedimento(models.Model):
    CONSULTA = 'CO'
    RETORNO = 'RE'
    CHECKUP = 'CH'

    PROCEDIMENTO_ESCOLHA = [
        (CONSULTA, 'Consulta'),
        (RETORNO, 'Retorno'),
        (CHECKUP, 'Check-up Geral')
    ]
    procedimento = models.CharField(max_length=2, choices=PROCEDIMENTO_ESCOLHA, default=CONSULTA, verbose_name='Procedimento')
    data_execucao = models.DateField(null=True, blank=True, verbose_name='Data de Execução')
    paciente = models.ForeignKey(pessoa, null=True, on_delete=models.CASCADE, related_name='paciente', verbose_name='Paciente')
    medico = models.ForeignKey(pessoa, null=True, on_delete=models.CASCADE, related_name='medico', verbose_name='Médico')

    def __str__(self):
        return self.procedimento

    class Meta:
        ordering = ['procedimento', 'data_execucao',]