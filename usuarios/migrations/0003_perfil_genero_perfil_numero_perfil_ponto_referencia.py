# Generated by Django 5.1 on 2024-09-26 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_perfil_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='genero',
            field=models.CharField(blank=True, choices=[('MASC', 'Masculino'), ('FEM', 'Feminino'), ('OTHER', 'Outros')], max_length=200, null=True, verbose_name='Gênero'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='numero',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='ponto_referencia',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Ponto de Referência'),
        ),
    ]
