# Generated by Django 5.1 on 2024-09-07 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_produto_estoque'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100, verbose_name='Preço'),
        ),
    ]
