# Generated by Django 4.1.5 on 2023-02-10 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0004_alter_pessoa_ativo_alter_pessoa_celular_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='procedimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procedimento', models.CharField(choices=[('CO', 'Consulta'), ('RE', 'Retorno'), ('CH', 'Check-up Geral')], default='CO', max_length=2, verbose_name='Procedimento')),
                ('data_execucao', models.DateField(blank=True, null=True, verbose_name='Data de Execução')),
                ('medico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medico', to='pessoas.pessoa', verbose_name='Médicos')),
                ('paciente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to='pessoas.pessoa', verbose_name='Pacientes')),
            ],
            options={
                'ordering': ['procedimento', 'data_execucao'],
            },
        ),
    ]
