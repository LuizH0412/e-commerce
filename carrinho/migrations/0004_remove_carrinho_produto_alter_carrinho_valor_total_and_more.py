# Generated by Django 5.1 on 2024-09-09 20:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0003_alter_carrinho_usuario'),
        ('produtos', '0004_alter_produto_preco'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrinho',
            name='produto',
        ),
        migrations.AlterField(
            model_name='carrinho',
            name='valor_total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=100, null=True, verbose_name='Valor Total'),
        ),
        migrations.CreateModel(
            name='ItemCarrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=1, verbose_name='Quantidade')),
                ('carrinho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='carrinho.carrinho', verbose_name='Carrinho')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.produto', verbose_name='Produtos')),
            ],
        ),
    ]
