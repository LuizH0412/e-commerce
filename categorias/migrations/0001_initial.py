# Generated by Django 5.1 on 2024-09-05 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('descricao', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descrição')),
            ],
        ),
    ]
