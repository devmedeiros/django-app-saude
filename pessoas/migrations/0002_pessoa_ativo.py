# Generated by Django 4.1.5 on 2023-02-08 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
    ]
